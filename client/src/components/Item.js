class Item {
  constructor(name = '', cost = 0.0) {
      this.name = name;
      this.cost = cost;
      this.peoples = null;
  }

  // Additional methods if needed
  display() {
      return `${this.name} - $${this.cost.toFixed(2)}`;
  }
}

export default Item;