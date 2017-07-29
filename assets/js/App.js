import React, { Component } from 'react';
import SearchPage from './SearchPage';
import AccountPage from './AccountPage';
import BuyMealPage from './BuyMealPage';
import AddCreditPage from './AddCreditPage';


class App extends Component {
    constructor () {
        super();
        this.state = {
            currentView: 'searchpage',
            currentAccount: null,
            accounts: [
                {
                    name: 'John Doe',
                    id: '1',
                    lastCredit: '7/20/17',
                    lastMeal: '5/30/17',
                    currentCredit: 4.25
                },
                {
                    name: 'Josey',
                    id: '2',
                    lastCredit: '7/20/17',
                    lastMeal: '5/30/17',
                    currentCredit: 1.75
                },
                {
                    name: 'J Odin',
                    id: '3',
                    lastCredit: '7/20/17',
                    lastMeal: '5/30/17',
                    currentCredit: 3.00
                },
            ]
        };
    }

    switchView (viewname, account) {
        this.setState({
            currentView: viewname,
            currentAccount: account
        });
    }

    updateCredit (newCredit) {
        this.state.currentAccount.currentCredit = newCredit;
    }

    render () {
        const {
             currentView,
             currentAccount,
             accounts
         } = this.state;

         if (currentView === 'searchpage') {
            return (
                <SearchPage switchView={(viewname, account) => this.switchView(viewname, account)}
                            accounts={accounts}/>
            )
         } else if (currentView === 'accountpage') {
            return (
                <AccountPage switchView={(viewname, account) => this.switchView(viewname, account)}
                             account={currentAccount} />
            );
         } else if (currentView === 'addcreditpage') {
            return (
                <AddCreditPage switchView={(viewname, account) => this.switchView(viewname, account)} 
                               account={currentAccount}
                               updateCredit={(newCredit) => this.updateCredit(newCredit)} />
            )
         } else if (currentView === 'buymealpage') {
            return (
                <BuyMealPage switchView={(viewname, account) => this.switchView(viewname, account)}
                             account={currentAccount}
                             updateCredit={(newCredit) => this.updateCredit(newCredit)} />
            )
         }
    }
}

export default App;
