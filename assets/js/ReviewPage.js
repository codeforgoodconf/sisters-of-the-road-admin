import React, { Component } from 'react';
import AccountSummary from './AccountSummary';
import axios from 'axios'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

class ReviewPage extends Component {
    constructor (props) {
        super(props);
        this.state = {}
        this.addCredit = this.addCredit.bind(this)
        this.handleInput = this.handleInput.bind(this)
    }
    addCredit () {
        let amount = Number(this.props.pendingTransaction) * 100;
        debugger
        console.log(this.state.initials)
        let id = this.props.account.id
        axios.post('/account/' + id + '/credit', {amount: amount, initials: this.state.initials})
        .then((response) => {
        this.props.switchView('confirmationpage', this.props.account)
        }).catch((response) => {
            
        })
    }

    handleInput(e) {
        this.setState({initials: e.target.value})
    }

    render () {
        const {
            account,
            pendingTransaction
        } = this.props;
        
        return (
            <div class="ReviewPage">
                <AccountSummary account={account} switchView={this.props.switchView} />
                <div id="calculate" class="fl w-50 mt5 ba bw1 pa2">
                    <div class="total"><p class='f1'>Review Your Order</p>
                        {pendingTransaction > 0 &&
                            <h2 class="tl">Amount to add: ${(pendingTransaction).toFixed(2)}</h2>
                        }
                        {pendingTransaction == 0 &&
                            <h2 class="tl">Amount is zero!</h2>
                        }
                        {pendingTransaction < 0 &&
                            <h2 class="tl">Amount to spend: ${(pendingTransaction * -1).toFixed(2)}</h2>
                        }
                        <h2 class="tl">New balance: ${((account.currentCredit / 100) + pendingTransaction).toFixed(2)}</h2>
                    </div>
                    <form>
                        <label class="f3 b dib tr">Customer Initials:</label>
                        <input id="initials"
                        class="ml2 pa2 f4 w-60 input-reset ba bg-transparent hover-bg-light-gray"
                        type="string"
                        // value={this.state.amount}
                        placeholder={"Enter your initials"}
                        onChange={this.handleInput} 
                        />
                    </form>
                    
                </div>
    
                <div class="mt5 fr w-50 h-50">
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 fl bg-light-gray blue w-40"
                        onClick={() => this.props.switchView('accountpage', account)}>
                        <i class="fas fa-times pr2"></i>Cancel
                    </button>
                    <button class="f4 br0 ph3 pv2 mb2 mr3 dib h3 w-50 fr white bg-green"
                            onClick={ this.addCredit }>
                        <i class="fas fa-plus pr2"></i>Confirm
                    </button>
                </div>
            </div>
         );
    }
}

export default ReviewPage;
