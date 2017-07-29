import React, { Component } from 'react';
import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

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
         var amount = hours * HOUR_MULIPLIER;
         axios.post('/account/1/add', {amount: amount}).then(function(response) {
             if (response.data && response.data.result === 'ok') {
                updateCredit(account.currentCredit + amount);
                switchView('accountpage', account);
             } else {
                 // the account ID was not found - what to do?
                 console.log('no account!')
             }
         });
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
                    <h5>Last worked: {account.lastCredit}</h5>
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
                    <button type="submit" className="btn btn-success col-sm-offset-5 center-block" onClick={() => this.addCredit(account, hours)}>
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
