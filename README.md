# Project-PDS
Track: Open Innovation
Cognition hackathon

Welcome to Project-PDS

As of now we have almost completed the frontend part of our project.
We have used HTML, CSS, Javascript, SCSS, Bootstrap 5.

Our Project currently includes two dashboards
     - one dashboard for the central entity that monitors all of the retail outlets that fall inside the boundaries of the authority
     - another dashboard for each of the ration outlets that deal directly with the public
     

Since our project is a prototype, we are going to focus on Chennai corporation, but the functionality can be modelled to a much much bigger area as well. The idea remains the same.

Let us take a closer look at each of the dashboards

The central dashboard:


![dsb](https://user-images.githubusercontent.com/78302047/183239554-be177c64-9b43-400c-a6e4-c8a9fcb23288.jpg)

![image](https://user-images.githubusercontent.com/78302047/183239849-a944e0e3-5bcd-4858-bac7-9412d4a22752.png)


The central dashboard derives the data from the smart contract implemented in the blockchain. The smart contract running on the blockchain is constantly updating the values owing to the transactions happening at the ration outlets. The dashboard will be used by the officials to monitor the transactions happening at all the outlets and will help them take informed decisions regarding the surplus of food grains, if any, generated at the outlets, thus leading to effecient food management. The smart contract ensures that all the transactions are accounted for.


The ration outlet dashboard:
     This folder consists of the screen that is visible in every ration shop.
     ![dashboard](https://user-images.githubusercontent.com/98336464/183240266-88c19c97-b376-4d62-905d-699fde3ac20c.png)
It is the personalized dashboard for ration shopkeepers and can give details of the monthly allocated stocks for that shop and for the individual people that is to be given.
     it is retrived from blockchain and confirmed by smart contracts.


The 'beneficiaries claim' form given at the bottom is to mimic the swiping of the 'advanced' ration card that contains the information of the beneficiary, his amount of ration he is entitled to among other information.

This advanced ration card is connected directly to the blockchain and transactions made through this card will be reflected in the smart contract running in the blockchain. A detailed information on the working of this 'advanced' ration card will be given at a later stage of the project. 




