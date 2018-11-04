import React, { Component } from 'react';
import axios from 'axios';
import DollarInput from './DollarInput';
import AccountSummary from './AccountSummary';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


class AddCreditPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    

    updateAmount (amount) {
        this.setState({amount: amount});
    }

    render () {
        const {
            account
        } = this.props;

        return (
            <div class="AddCreditPage">
                <AccountSummary account={account} switchView={this.props.switchView}/>
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <h1>Add Credit</h1>
                    <DollarInput updateAmount={(amount) => this.updateAmount(amount)} />
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={() => this.props.switchView('accountpage', account)}>
                        <i class="fas fa-times pr2"></i>Cancel
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-green"
                            onClick={() => {
                                this.props.updateTransactionAmount(parseInt(this.state.amount));
                                return this.props.switchView('reviewpage', account)
                                }
                                }>
                        <i class="fas fa-plus pr2"></i>Continue
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
