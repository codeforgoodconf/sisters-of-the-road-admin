import React, { Component } from 'react';
import AccountSummary from './AccountSummary';


class AccountPage extends Component {
    constructor (props) {
        super(props);
        this.navigate = this.navigate.bind(this)
        this.props.clearSearchQuery()

    }

    navigate(url) {
        return () => this.props.history.push(url)
    }


    render () {
        
        
        return (
            <div className="AccountPage">
                <AccountSummary account={this.props.account} action={this.navigate('/')}/>

                <div className="mt5 fr w-50 h-50">
                    <button className="f3 br0 ph3 pv0 mb4 db h-25 w-80 white bg-purple"
                            onClick={this.navigate('/buycard')}>
                        <i className="far fa-credit-card pr2"></i>Buy Card 
                    </button>
                    <button className="f3 br0 ph3 pv1 mb4 db h-25 w-80 white bg-purple"
                            onClick={this.navigate('/buymeal')}>
                        <i className="fas fa-utensils pr2"></i>Buy Meal
                    </button>
                    <button className="f3 br0 ph3 pv1 mb0 db h-25 w-80 white bg-green"
                            onClick={() => this.props.switchView('addcreditpage', account)}>
                        <i className="fas fa-plus pr2"></i>Add Credit
                    </button>
                </div>
            </div>
         );
    }
}

export default AccountPage;
