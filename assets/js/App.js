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
            accounts: []
        };
        axios.get('/account/list').then((response) => {
            let accounts = [];
            response.data.forEach((dbaccount, index) => {
                accounts.push({
                    name: dbaccount.Name,
                    id: String(index),
                    lastCredit: "5/3/2017",
                    lastMeal: "3/20/17",
                    currentCredit: dbaccount.Balance
                });
            });
            this.setState({accounts: accounts});
        });
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
