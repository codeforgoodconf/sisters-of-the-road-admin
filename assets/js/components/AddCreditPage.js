import React, { Component } from 'react';

import AccountSummary from './AccountSummary'
import DollarInput from './DollarInput';



class AddCreditPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
        this.navigate = this.navigate.bind(this);
        this.addCredit = this.addCredit.bind(this);
        this.updateAmount = this.updateAmount.bind(this);
    }

    navigate(url) {
        return () => this.props.history.push(url)
    }

    addCredit () {
        const nav = () => {
            this.props.history.push('/account')
        }

        
        const that = this
        this.props.action(this.props.account, Number(this.state.amount))
        .then(() => {

            if (!that.props.error) nav()
        })
    }

    updateAmount (e) {
        this.setState({amount: e.target.value});
    }

    render () {

        let error = this.props.error
        if (error === 'limit_error') {
            error = "Balance can't exceed $50"
        } else if  (error === "input_error") {
            error = "Please enter an amount above $0 in increment of $.25";
        }

        return (
            <div className="AddCreditPage">
                <AccountSummary account={this.props.account} action={this.navigate('/')}/>
                <div id="calculate" className="fl w-50 mt5 ba bw1 pa2">
                    <h1>Add Credit</h1>
                    <DollarInput updateAmount={this.updateAmount} amount={this.state.amount} error={error} />
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={this.navigate('/account')}>
                        <i className="fas fa-times pr2"></i>Cancel
                    </button>
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-green"
                            onClick={this.addCredit}>
                        <i className="fas fa-plus pr2"></i>Add amount
                    </button>
                </div>
            </div>
         );
    }
}

export default AddCreditPage;
