pragma solidity >=0.4.22 <0.6.0;
contract Test {
    struct company {
        string name;
        bool isBank;
    }
    struct receipt {
        uint loan;
        string lender;
        string borrower;
        uint recordedDate;
        uint payDate;
        bool paid;
    }

    address bank;
    mapping(string => company) companys;
    
    uint numReceipts;
    mapping(uint => receipt) receipts;
    
    event record(uint loan,string lender,string borrower,uint recordedDate,uint payDate,bool paid);
    
    constructor() public {
        bank = msg.sender;
        numReceipts=0;
        companys["bank"]=company("bank",true);
        companys["car"]=company("car",false);
        companys["tire"]=company("tire",false);
        companys["hub"]=company("hub",false);
    }

    function AccountReceivableCreate(string lender,string borrower,uint amount,uint dateToPay) public {
        numReceipts++;
        receipts[numReceipts]=receipt(amount,lender,borrower,now,dateToPay,false);
        emit record(receipts[numReceipts].loan,receipts[numReceipts].lender,receipts[numReceipts].borrower,receipts[numReceipts].recordedDate,receipts[numReceipts].payDate,receipts[numReceipts].paid);
    }

    ///find receipt by receiptID
    function AccountReceivableTransfer(uint receiptID,string lender,string borrower,uint amount,uint dateToPay) public{
        
        receipts[receiptID].loan-=amount;
        numReceipts++;
        receipts[numReceipts]=receipt(amount,lender,receipts[receiptID].borrower,now,dateToPay,false);
        emit record(receipts[numReceipts].loan,receipts[numReceipts].lender,receipts[numReceipts].borrower,receipts[numReceipts].recordedDate,receipts[numReceipts].payDate,receipts[numReceipts].paid);
    }
    
    function AccountReceivableFinancing(uint receiptID) public{
        
        numReceipts++;
        receipts[numReceipts]=receipt(receipts[receiptID].loan,"bank",receipts[receiptID].borrower,now,receipts[receiptID].payDate,false);
        emit record(receipts[numReceipts].loan,receipts[numReceipts].lender,receipts[numReceipts].borrower,receipts[numReceipts].recordedDate,receipts[numReceipts].payDate,receipts[numReceipts].paid);
    }
    
    function AccountReceivablePay(uint receiptID) public{
        if(receipts[receiptID].payDate>=now){
            receipts[receiptID].paid=true;
        }
        emit record(receipts[receiptID].loan,receipts[receiptID].lender,receipts[receiptID].borrower,receipts[receiptID].recordedDate,receipts[receiptID].payDate,receipts[receiptID].paid);
    }
}
