import { combineReducers } from 'redux';

import searchQueryReducer from './search_query'
import accountReducer from './account'


const entitiesReducer = combineReducers({
    "searchQuery": searchQueryReducer,
    "account": accountReducer
});


export default entitiesReducer;