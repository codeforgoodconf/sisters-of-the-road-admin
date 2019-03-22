import React, { Component } from 'react';

import DollarInput from './DollarInput';
import AccountSummary from './AccountSummary';


class BuyCardPage extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
        this.navigate = this.navigate.bind(this);
        this.buy = this.buy.bind(this);
        this.updateAmount = this.updateAmount.bind(this);
    }

    navigate(url) {
        return () => this.props.history.push(url)
    }
    buy () {
        const nav = () => {
            this.props.history.push('/account')
        }
        const that = this
        this.props.action(this.props.account, Number(this.state.amount))
        .then(() => {
            debugger
            if (!that.props.error) nav()
        })
    }

    updateAmount (e) {
        this.setState({amount: e.target.value});
    }

    render () {
        
        let error = this.props.error
        if (error === 'limit_error') {
            error = "Balance can't go below $0"
        } else if  (error === "input_error") {
            error = "Please enter an amount above $0 in increment of $.25";
        }

        return (
            <div className="BuyCardPage">
                <AccountSummary account={this.props.account} action={this.navigate('/')}/>
                <div id="calculate" className="fl w-50 mt5 ba bw1 pa2">
                    <h1>{this.props.title}</h1>
                    <DollarInput updateAmount={this.updateAmount} amount={this.state.amount} error={error} /> 
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={this.navigate('/account')}>
                        <i className="fas fa-times pr2"></i>Cancel
                    </button>
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-purple"
                            onClick={this.buy}>
                        <i className="fas fa-minus pr2"></i>
                        Spend amount
                    </button>               
                </div>
            </div>
         );
    }
}

export default BuyCardPage;
