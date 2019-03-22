import React, { Component } from 'react';
import { Switch, HashRouter, Route, withRouter } from 'react-router-dom';
import { Provider } from 'react-redux'

import { SelectedRoute } from '../utils/route_util'

import SearchPage from './SearchPageContainer';
import AccountPage from './AccountPageContainer';
import BuyMealPage from './BuyMealContainer';
import BuyCardPage from './BuyCardContainer';
import AddCreditPage from './AddCreditContainer';
import ConfirmationPage from './ConfirmationPage';



const App = ({ store }) => (
    <Provider store={ store } >
        <HashRouter>
            <Switch>
                <SelectedRoute exact path='/account' component = {AccountPage} />
                <SelectedRoute exact path='/buycard' component = {BuyCardPage} />
                <SelectedRoute exact path='/buymeal' component = {BuyMealPage} />
                <SelectedRoute exact path='/credit' component = {AddCreditPage} />
                <Route path='/' component = {SearchPage} />
            </Switch>

        </HashRouter>
    </Provider>
)



// class App extends Component {
//     constructor () {
//         super();
//         this.state = {
//             currentView: 'searchpage',
//             currentAccount: null
//         };
//     }

//     switchView (viewname, account) {
//         this.setState({
//             currentView: viewname,
//             currentAccount: account
//         });
//     }

//     updateBalance (amount) {
//         this.state.currentAccount.currentCredit += amount;
//         this.state.currentAccount.lastAdded = amount;
//     }

//     updateSearchQueryNotified(searchQuery){
//         this.setState({searchQuery:searchQuery});
//     }
//     render () {
//         const {
//              currentView,
//              currentAccount,
//              searchQuery
//          } = this.state;

//          if (currentView === 'searchpage') {
//             return (
//                 <SearchPage switchView={(viewname, account) => this.switchView(viewname, account)} 
//                  searchQuery={searchQuery} onSearchQueryValueChangeNotify = {this.updateSearchQueryNotified}/>
//             )
//          } else if (currentView === 'accountpage') {
//             return (
//                 <AccountPage switchView={(viewname, account) => this.switchView(viewname, account)}
//                              account={currentAccount} />
//             );
//          } else if (currentView === 'addcreditpage') {
//             return (
//                 <AddCreditPage switchView={(viewname, account) => this.switchView(viewname, account)}
//                                account={currentAccount}
//                                updateBalance={(newCredit) => this.updateBalance(newCredit)} />
//             )
//          } else if (currentView === 'buymealpage') {
//             return (
//                 <BuyMealPage switchView={(viewname, account) => this.switchView(viewname, account)}
//                              account={currentAccount}
//                              updateBalance={(newCredit) => this.updateBalance(newCredit)} />
//             )
//          } else if (currentView === 'buycardpage') {
//             return (
//                 <BuyCardPage switchView={(viewname, account) => this.switchView(viewname, account)}
//                              account={currentAccount}
//                              updateBalance={(newCredit) => this.updateBalance(newCredit)} />
//             )
//          } else if (currentView == "confirmationpage") {
//              return (
//                  <ConfirmationPage switchView={(viewname, account) => this.switchView(viewname, account)}
//                              account={currentAccount}/>
//              )
//          }
//     }
// }

export default App;
