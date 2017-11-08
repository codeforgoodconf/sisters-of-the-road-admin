import React, { Component } from 'react';



class SearchPage extends Component {
    constructor () {
        super();
        this.state = {
            accounts: [],
            searchQuery: ''
        };
    }

    onSearchChange (value) {
        this.setState({searchQuery: value});
    }

    searchAccounts () {
        axios.get('/account/search?q=' + this.state.searchQuery).then((response) => {
            let accounts = [];
            response.data.forEach((account, index) => {
                accounts.push({
                    name: account.name,
                    id: account.account_id,
                    lastCredit: account.last_add,
                    lastMeal: account.last_subtract,
                    currentCredit: Number(account.balance)
                });
            });
            this.setState({accounts: accounts});
        });
    }

    render () {
        const {
            accounts,
            searchQuery
        } = this.state;
        return (
            <div class="SearchPage">
                <div class="form-group">
                    <div id="searchbar" class="input-group">
                        <input class="input-lg center-block form-control"
                               type="text"
                               placeholder="Search barter accounts"
                               onChange={(event) => this.onSearchChange(event.target.value)}/>
                        <span class="input-group-btn">
                            <button class="btn btn-lg btn-default" type="button"
                                    onClick={() => this.searchAccounts(searchQuery)}>
                                Search
                            </button>
                        </span>
                    </div>
                </div>
                <div class="row">
                    <ul class="list-group">
                    {accounts.map((account) =>
                        <li class="list-group-item row"
                            onClick={() => this.props.switchView('accountpage', account)}
                            key={account.id}>
                            <p class="col-sm-4"> {account.name} </p>
                            <p class="col-sm-4">Last credit: {account.lastCredit}</p>
                            <p class="col-sm-4">Last purchase: {account.lastMeal}</p>
                        </li>
                    )}
                    </ul>
                </div>
            </div>
         );
    }
}

export default SearchPage;
