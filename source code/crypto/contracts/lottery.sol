pragma solidity ^0.8;
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract lottery is VRFConsumerBase {
//bytes32 public requestId;
uint256 public randomResult;
uint public winnerIndex;
    bytes32 internal keyHash;
    uint256 internal fee;
    uint public entryPriceInCents;
    
    address payable[] public players;
    address owner;
    enum LOTTERY_STATE {
        CLOSED,
        OPEN,
        CALCULATING_WINNER
    }
    LOTTERY_STATE public lottery_state;

    constructor() VRFConsumerBase(0xb3dCcb4Cf7a26f6cf6B120Cf5A73875B7BBc655B,0x01BE23585060835E02B77ef475b0Cc51aA1e0709) {
        owner = msg.sender;
        entryPriceInCents = 500;
        lottery_state = LOTTERY_STATE.CLOSED;
        keyHash = 0x2ed0feb3e7fd2022120aa84fab1945545a9f2ffc9076fd6156fa96eaff4c1311;
        fee = 0.1 * 10 ** 18;
    }
    
    modifier onlyOwner {
        require(msg.sender==owner,'ur not the owner');
        _;
    }    

    function enter() public payable {
        (uint lowerBound,uint upperBound) = calBounds();
        require(lottery_state==LOTTERY_STATE.OPEN,'lottery has yet to open');
        require(msg.value>lowerBound && msg.value<upperBound,'input the equivalent of $5 in ether to enter');
        players.push(payable(msg.sender));

    }

    function getEntranceFee() public view returns(uint,uint,uint){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);

        (,int price,,,)= priceFeed.latestRoundData();
            uint8 decimals = priceFeed.decimals();
    uint priceUint = uint(price);
        uint entryPriceInWei = (entryPriceInCents*10**18)/(priceUint/(10**(decimals-2)));
        return (entryPriceInWei,priceUint,decimals);


    }

    function calBounds() public view returns(uint,uint){
        (uint entryPriceInWei,uint priceUint,uint decimals)=getEntranceFee();
        uint tolerance = (5*10**18)/(priceUint/(10**(decimals-2)));
        uint lowerBound = entryPriceInWei - tolerance;
        uint upperBound = entryPriceInWei + tolerance;
        return (lowerBound,upperBound);
    }

    function startLottery() public onlyOwner {
        require(lottery_state==LOTTERY_STATE.CLOSED,'lottery still in progress');
        lottery_state=LOTTERY_STATE.OPEN;
    }

    function findWinner() public onlyOwner {
        lottery_state = LOTTERY_STATE.CALCULATING_WINNER;
        
        //fulfillRandomness(bytes32 requestId, uint256 randomness);
        
    }

    function getRandomNumber() public returns (bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "insufficient link");
        return requestRandomness(keyHash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        require(lottery_state==LOTTERY_STATE.CALCULATING_WINNER,'not yet cal time...');
        //require(randomness>0,'rng must be >0');
        randomResult = randomness;
        winnerIndex = randomResult % players.length;
        address winner = players[winnerIndex];
        payable(winner).transfer(address(this).balance);

        players = new address payable[](0);
        lottery_state = LOTTERY_STATE.CLOSED;
    }

    function withdrawLink() public payable onlyOwner {
        payable(owner).transfer(address(this).balance);
        
    }
}