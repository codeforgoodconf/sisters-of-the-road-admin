import React, { Component } from 'react';


class BuyMealPage extends Component {
    constructor () {
        super();
    }

    render () {
         return (
            <div className="BuyMealPage">
                <div>
                    <h3>Customer Name</h3>
                    <h5>Last worked: date</h5>
                    <h5>Last meal: date</h5>
                </div>
                <div>
                    Meal Total: 
                    <input type="number" min="0.00" step="0.25" max="2500" />
                </div>
                <div>
                    <button>
                        Spend amount
                    </button>
                </div>
                <button onClick={() => this.props.switchView('accountpage')}>
                    Cancel
                </button>
            </div>
         );
    }
}

export default BuyMealPage;
