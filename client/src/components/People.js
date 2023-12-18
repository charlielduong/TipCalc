// Person.js
export class Person {
  constructor() {
      this.name = "Enter name here";
      this.items = [];
      this.costs = [];
      this.addedCurrentItem = false;
  }

  addCost(cost){
    this.costs.push(cost);
  }

  removeCost(){
    this.costs.pop;
  }
  // Additional methods or properties for the Person class
}
