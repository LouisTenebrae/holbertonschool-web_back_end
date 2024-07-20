export default class Building {
    /**
         * @param {Number} sqft
         */
    constructor(sqft) {
      this._sqft = sqft;
      if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  
    get sqft() {
      return this._sqft;
    }
  }