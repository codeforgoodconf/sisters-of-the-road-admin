import { combineReducers } from 'redux';

import searchQueryReducer from './search_query'


const entitiesReducer = combineReducers({
    "searchQuery": searchQueryReducer
});


export default entitiesReducer;