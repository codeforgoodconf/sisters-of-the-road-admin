import React, { Component } from 'react';


const HOUR_MULIPLIER = 3.0;


class AddCreditPage extends Component {
    constructor () {
        super();
        this.state = {
            hours: 0
        };
    }

    addCredit (account, hours) {
        const {
            updateCredit,
            switchView
         } = this.props;
         updateCredit(account.currentCredit + hours * HOUR_MULIPLIER);
         switchView('accountpage', account);
    }

    render () {
        const {
            account
        } = this.props;

        var hours;

        return (
            <div className="AddCreditPage">
                <div className="header col-sm-12 centered">
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastWorked}</h5>
                    <h5>Last meal: {account.lastMeal}</h5>
                </div>
                <div id="calculate" className="jumbotron row center-block">
                    <div className="total">
                        <h3 className="text-center">Hours Worked:</h3>
                        <input id="hours"
                               className="numbers col-sm-offset-3 input-lg center-block text-center"
                               type="number"
                               min="0.00"
                               step="0.25"
                               max="2500"
                               onChange={(event) => hours = event.target.value} />
                    </div>
                </div>
                <div>
                    <button className="btn btn-success col-sm-offset-5 center-block" onClick={() => this.addCredit(account, hours)}>
                        Add amount
                    </button>
                </div>
                <div>
                    <button className="btn btn-info col-sm-2 col-sm-offset-5" onClick={() => this.props.switchView('accountpage', account)}>
                        Cancel
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
