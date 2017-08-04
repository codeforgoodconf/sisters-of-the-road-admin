import React, { Component } from 'react';
import axios from 'axios';


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";



class AddCreditPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    addCredit (account) {
        const {
            updateBalance,
            switchView
         } = this.props;
         let amount = Number(this.state.amount) * 100;
         axios.post('/account/' + account.id + '/add', {amount: amount}).then(function(response) {
             if (response.data && response.data.result === 'ok') {
                updateBalance(amount);
                switchView('confirmationpage', account);
             } else {
                 // the account ID was not found - what to do?
                 console.log('no account!')
             }
         });
    }

    onAmountChange (amount) {
        if (amount === undefined) {
            return;
        }

        let amountStr = String(amount).replace('.', ''),
            len = amountStr.length;
        if (len === 1) {
            amountStr = amountStr + '.00';
        } else if (len === 2) {
            amountStr = amountStr.slice(0, 1) + '.' + amountStr.slice(1, 2) + '0';
        } else {
            amountStr = amountStr.slice(0, len - 2) + '.' + amountStr.slice(len - 2, len);
        }

        if (isNaN(Number(amountStr))) {
            this.setState({amount: ''});
        } else {
            this.setState({amount: Number(amountStr)});
        }
    }

    render () {
        const {
            account
        } = this.props;

        return (
            <div className="AddCreditPage">
                <div className="header col-sm-12 centered">
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastCredit}</h5>
                    <h5>Last purchase: {account.lastMeal}</h5>
                </div>
                <div id="calculate" className="jumbotron row center-block">
                    <div className="total">
                        <h3 className="text-center">Amount to add:</h3>
                        <input id="amount"
                            className="numbers col-sm-offset-3 input-lg center-block text-center"
                            type="number"
                            min="0"
                            step="0.25"
                            value={this.state.amount}
                            placeholder={0}
                            onChange={(event) => this.onAmountChange(event.target.value)} /> 
                    </div>
                </div>
                <div>
                    <button type="submit"
                            className="btn btn-success col-sm-offset-5 center-block"
                            onClick={() => this.addCredit(account)}>
                        Add amount
                    </button>
                </div>
                <div>
                    <button className="btn btn-info col-sm-2 col-sm-offset-5"
                            onClick={() => this.props.switchView('accountpage', account)}>
                        Cancel
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
