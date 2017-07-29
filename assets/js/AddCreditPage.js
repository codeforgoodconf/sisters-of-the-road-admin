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
                <div>
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastWorked}</h5>
                    <h5>Last meal: {account.lastMeal}</h5>
                </div>
                <div>
                    Hours Worked: 
                    <input type="number" min="0.00" step="0.25" max="2500" 
                           onChange={(event) => hours = event.target.value} />
                </div>
                <div>
                    <button onClick={() => this.addCredit(account, hours)}>
                        Add amount
                    </button>
                </div>
                <button onClick={() => this.props.switchView('accountpage', account)}>
                    Cancel
                </button>
            </div>
         );
    }
}

export default AddCreditPage;
