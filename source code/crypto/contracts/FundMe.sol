pragma solidity >=0.6.6 <0.9.0;
//interface compile down to application binary interface
//must use abi to interact with alr deployed smart contract
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    address owner;
    constructor() {
        owner = msg.sender;
    }
    //tracks individual senders sent value
    mapping(address => uint) public addressToAmountFunded;
    function fund() public payable {
        //msg.value = no wei sent by sender (with the msg)
        //msg.sender = address of sender
        uint256 minimumUSD = 50 * 10 ** 18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");
        addressToAmountFunded[msg.sender] += msg.value;
    }
   
   function getPrice() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
         return uint256(answer * 10000000000);
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    modifier onlyOwner {
        require(msg.sender==owner,'ur not the owner');
        _;
    }
    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
        
    }
  
}