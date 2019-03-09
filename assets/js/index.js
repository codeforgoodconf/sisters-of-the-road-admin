import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import configureStore from './store'
import { requestSearchQuery, buyCard } from './actions/account_actions'

document.addEventListener('DOMContentLoaded', () => {
  

  const store = configureStore()
  // for testing actions/reducers
  window.getState = store.getState
  window.dispatch = store.dispatch
  window.requestSearchQuery = requestSearchQuery
  window.buyCard = buyCard

  ReactDOM.render(
    <App store={store} />,
    document.getElementById('root')
  );
})


