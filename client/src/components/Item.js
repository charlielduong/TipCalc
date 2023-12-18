import People from './People'
class Item {
    constructor(name = '', cost = 0.0) {
        this.name = name;
        this.cost = cost;
        this.peoples = [];
        this.currentCost = cost;
    }

    // Additional methods if needed
    display() {
        return `${this.name} - $${this.cost.toFixed(2)}`;
    }

    addPeople(person){
      if(person instanceof People){
        this.peoples.push(person);
        this.currentCost = cost / peoples.length;
        this.person.addCost(this.currentCost);
      }
    }

    removePeople(person){
      if(person instanceof People){
        this.peoples.pop
        this.currentCost = cost / peoples.length;
      }
    }
  }
export default Item;