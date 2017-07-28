import React, { Component } from 'react';
import SearchPage from './SearchPage';
import AccountPage from './AccountPage';
import BuyMealPage from './BuyMealPage';
import AddCreditPage from './AddCreditPage';


class App extends Component {
    constructor () {
        super();
        this.state = {
            currentView: 'searchpage'
        };
    }

    switchView (viewname) {
        this.setState({currentView: viewname});
    }

    render () {
        const {
             currentView
         } = this.state;

         if (currentView === 'searchpage') {
            return (
                <SearchPage switchView={(viewname) => this.switchView(viewname)}/>
            )
         } else if (currentView === 'accountpage') {
            return (
                <AccountPage switchView={(viewname) => this.switchView(viewname)}/>
            );
         } else if (currentView === 'addcreditpage') {
            return (
                <AddCreditPage switchView={(viewname) => this.switchView(viewname)} />
            )
         } else if (currentView === 'buymealpage') {
            return (
                <BuyMealPage switchView={(viewname) => this.switchView(viewname)} />
            )
         }
    }
}

export default App;
