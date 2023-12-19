// Person.js
export class People {
  constructor() {
      this.name = "";
      this.items = [];
      this.costs = [];
  }

  addCost(cost){
    this.costs.push(cost);
  }

  removeCost(){
    this.costs.pop;
  }
  // Additional methods or properties for the People class
}
