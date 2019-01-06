import React, { Component } from 'react';


class AccountSummary extends Component {
    constructor () {
        super();
        this.state = {
        };
    }

    render () {
        return (
            <div id="account-summary" class="blue oswald ml4 pb4 fl w-40">
                <h1 class='f1'>{this.props.account.name}</h1>
                <p class="f2">
                    Current Balance:
                    <span class="gray"> ${this.props.account.currentCredit.toFixed(2)}</span>
                </p>

                <p class="f3">Last Worked: {this.props.account.lastCredit}</p>
                <p class="f3">Last Purchase: {this.props.account.lastMeal}</p>

                <button class="f4 ph3 pv2 mb2 mr3 dib h3 w-50 white bg-blue"
                    onClick={() => this.props.switchView('searchpage')}>
                        <i class="fas fa-angle-double-left pr2"></i>
                        Back to Search
                </button>
            </div>
         );
    }
}

export default AccountSummary;
