import React, { Component } from 'react';


class SearchPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            accounts
        } = this.props;
        return (
            <div className="SearchPage">
                I'm the search page!

                {accounts.map((account) =>
                    <div style={{borderStyle: 'solid', margin: '5px'}}
                         onClick={() => this.props.switchView('accountpage', account)}
                         key={account.id}>
                        <p>{account.name}</p>
                        <p>Last credit: {account.lastCredit}</p>
                        <p>Last meal: {account.lastMeal}</p>
                    </div>
                )}
            </div>
         );
    }
}

export default SearchPage;
