// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SmartContract{
    uint Totalallocation = 100;
    uint dispensed = 0;
    uint surplus = 100;
    address public authority;
    uint[] uids;

    struct beneficiary{
        uint alloc;
        uint sal;
    }

    mapping(uint=>beneficiary) public beneficiaries;

    constructor(){
        authority=msg.sender;
    }

    // only the authority can change allocations
    function changeAllocation(uint newAllocation) public{
        if(msg.sender==authority){
            Totalallocation = newAllocation;
        }
    }

    // only the authority can add beneficiaries
    function addBeneficiary(uint _uid, uint alloc, uint sal) public{
        if(msg.sender==authority){
            beneficiaries[_uid]=beneficiary(alloc, sal);
            uids.push(_uid);
        }
    }

    // the authority can change the individual allocations 
    function changeIndividualAllocation(uint threshold, uint change, int greater) public{
        require(msg.sender == authority , "Authority only access !");

        uint current;
        for(uint i=0 ; i < uids.length ; i++){
            current = uids[i];
            if(greater == 1){
                if(beneficiaries[current].sal > threshold){
                    beneficiaries[current].alloc = (((100 + change) / 100) * (beneficiaries[current].alloc)); 
                }
            }
            else{
                if(beneficiaries[current].sal < threshold){
                    beneficiaries[current].alloc = (((100 + change) / 100) * (beneficiaries[current].alloc));
                }
            }
        }
    }

    function getSurplus() public view returns(uint){
        return surplus;
    }

    function getDispensed() public view returns(uint){
        return dispensed;
    }

    function dispense(uint _uid) public{
        dispensed = dispensed + beneficiaries[_uid].alloc;
        surplus = surplus - beneficiaries[_uid].alloc; 
    }

    function showBeneficiaryAllocation(uint _uid) public view returns(uint){
        return beneficiaries[_uid].alloc;
    }

}
