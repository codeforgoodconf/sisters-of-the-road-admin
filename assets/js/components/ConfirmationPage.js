import React, { Component } from 'react';
import AccountSummary from './AccountSummary';


class ConfirmationPage extends Component {
    constructor (props) {
        super(props);
    }

    navigate(url) {
        return () => this.props.history.push(url)
    } 

    render () {
        
        return (
            <div class="ConfirmationPage">
                <AccountSummary account={this.props.account} action={this.navigate('/')}/>
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <div class="total"><p class='f1'>Changes Saved!</p>
                        <h2 class="tl">New balance: ${this.props.account.balance}</h2>
                    </div>
                </div>
                <div class="mt5 fr w-50 h-50">
                    <button class="f3 br0 ph3 pv0 mb4 db h-25 w-80 white bg-purple"
                            onClick={this.navigate('/')}>
                        <i class="far pr2"></i>Back to Account Summary 
                    </button>
                </div>
            </div>
         );
    }
}

export default ConfirmationPage;
