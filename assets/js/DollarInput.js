import React, {Component} from 'react';


class DollarInput extends Component {
    constructor() {
        super();
        this.state = {
            amount: ''
        };
    }

    onAmountChange(amount) {
        this.setState({amount: amount});
        this.props.updateAmount(amount);
    }

    render() {
        return (
            <form class="mb4 dib">
                <label class="f2">Amount $</label>
                <input id="amount"
                       class="ml2 pa2 f2 w-60 input-reset ba bg-transparent hover-bg-light-gray"
                       type="number"
                       min="0"
                       step="0.25"
                       value={this.state.amount}
                       placeholder={0}
                       onChange={(event) => this.onAmountChange(event.target.value)}/>
                <label class="fl f4 mt2 red" id="error-msg"></label>
            </form>
        );
    }
}

export default DollarInput;
