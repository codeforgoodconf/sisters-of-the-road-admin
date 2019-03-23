import React from 'react';
import { Switch, HashRouter, Route, withRouter } from 'react-router-dom';
import { Provider } from 'react-redux'

import { SelectedRoute } from '../utils/route_util'

import SearchPage from './SearchPageContainer';
import AccountPage from './AccountPageContainer';
import BuyMealPage from './BuyMealContainer';
import BuyCardPage from './BuyCardContainer';
import AddCreditPage from './AddCreditContainer';
import ConfirmationPage from './ConformationPageContainer';



const App = ({ store }) => (
    <Provider store={ store } >
        <HashRouter>
            <Switch>
                <SelectedRoute exact path='/account' component={AccountPage} />
                <SelectedRoute exact path='/buycard' component={BuyCardPage} />
                <SelectedRoute exact path='/buymeal' component={BuyMealPage} />
                <SelectedRoute exact path='/credit' component={AddCreditPage} />
                <SelectedRoute exact path='/conformation' component={ConfirmationPage} /> 
                <Route path='/' component = {SearchPage} />
            </Switch>

        </HashRouter>
    </Provider>
)

export default App;
