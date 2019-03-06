import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import configureStore from './store'
import { requestSearchQuery } from './actions/account_actions'

document.addEventListener('DOMContentLoaded', () => {
  

  const store = configureStore()
  // for testing actions/reducers

  window.getState = store.getState
  window.dispach = store.dispatch
  window.requestSearchQuery = requestSearchQuery

  ReactDOM.render(
    <App store={store} />,
    document.getElementById('root')
  );
})


