import React, { Component } from 'react';

import DollarInput from './DollarInput';
import AccountSummary from './AccountSummary';


class BuyCardPage extends Component {
    constructor (props) {
        super(props);
        this.state = {
            amount: "",
            initials: "",
            confirmError: ""
        };
        this.navigate = this.navigate.bind(this);
        this.showConfirm = this.showConfirm.bind(this);
        this.buy = this.buy.bind(this);
        this.updateAmount = this.updateAmount.bind(this);
        this.updateInitials = this.updateInitials.bind(this);
    }

    navigate(url) {
        return () => this.props.history.push(url)
    }

    showConfirm() {
        
        if (this.state.amount) {
            document.getElementById('confirm-modal').classList.remove('hidden')
        }
    }

    hideConfirm() {
        document.getElementById('confirm-modal').classList.add('hidden')
    }

    buy () {
        if (this.state.initials === "") return this.setState({confirmError: 'please enter your innitials'})
        const nav = () => {
            this.props.history.push('/conformation')
        }
        const that = this
        this.props.action(this.props.account, Number(this.state.amount), this.state.initials)
        .then(() => {
            
            if (!that.props.error) nav()
        })
    }

    updateAmount (e) {
        this.setState({amount: e.target.value});
    }

    updateInitials(e) {
        this.setState({initials: e.target.value})
    }

    render () {
        
        let error = this.props.error
        if (error === 'limit_error') {
            error = "Balance can't go below $0"
        } else if  (error === "input_error") {
            error = "Please enter an amount above $0 in increment of $.25";
        }
        let amount = this.state.amount === "" ? 0 : parseInt(this.state.amount).toFixed(2)
        return (

            
            <div className="BuyCardPage">
                <AccountSummary account={this.props.account} action={this.navigate('/')}/>

                <div id='confirm-modal' className="fl w-60 h-50 mt5 ba bw1 pa2 hidden" >
                    <h1>Confirm {this.props.title} - ${amount}</h1>
                    <form className="mb4 dib">    
                        <label className="f2">Initials</label>

                        <input id="amount"
                            className="ml2 pa2 f2 w-60 input-reset ba bg-transparent hover-bg-light-gray"
                            type="string"
                            value={this.state.initials}
                            onChange={this.updateInitials}
                            />
                        <label className="fl f4 mt2 red" id="error-msg">{this.state.confirmError}</label>           
                    </form>
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={this.hideConfirm}>
                        <i className="fas fa-times pr2"></i>Cancel
                    </button>
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-purple"
                            onClick={this.buy}>
                            
                        <i className="fas fa-minus pr2"></i>
                        Confirm
                    </button>
                </div>

                <div id="calculate" className="fl w-50 mt5 ba bw1 pa2">
                    <h1>{this.props.title}</h1>
                    <DollarInput updateAmount={this.updateAmount} amount={this.state.amount} error={error} /> 
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={this.navigate('/account')}>
                        <i className="fas fa-times pr2"></i>Cancel
                    </button>
                    <button className="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-purple"
                            onClick={this.showConfirm}>
                        <i className="fas fa-minus pr2"></i>
                        Spend amount
                    </button>               
                </div>
            </div>
         );
    }
}

export default BuyCardPage;
