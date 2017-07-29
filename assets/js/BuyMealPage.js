import React, { Component } from 'react';


class BuyMealPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            account
        } = this.props;
        return (
            <div className="BuyMealPage">
                <div className="header col-sm-12 centered">
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastWorked}</h5>
                    <h5>Last meal: {account.lastMeal}</h5>
                </div>
                <div id="calculate" className="jumbotron row center-block">
                    <div className="total">
                        <h3 className="text-center">Meal Total:</h3>
                        <input id="total" className="input-lg col-sm-offset-3 text-center center-block" type="number" min="0.00" step="0.25" max="2500" />
                    </div>
                </div>
                <div className="row">
                    <button className="btn btn-success col-sm-offset-5 center-block">
                        Spend amount
                    </button>
                </div>
                <button className="btn btn-info col-sm-offset-5 center-block" onClick={() => this.props.switchView('accountpage', account)}>
                    Cancel
                </button>
            </div>
         );
    }
}

export default BuyMealPage;
