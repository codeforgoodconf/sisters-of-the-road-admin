import React from 'react';
const DollarInput = ({amount, updateAmount, error}) => {
    return (
        <form className="mb4 dib">    
            <label className="f2">Amount $</label>
            <input id="amount"
                className="ml2 pa2 f2 w-60 input-reset ba bg-transparent hover-bg-light-gray"
                type="number"
                min="0"
                step="0.25"
                value={amount}
                placeholder={0}
                onChange={updateAmount} />
            <label className="fl f4 mt2 red" id="error-msg">{error}</label>           
        </form>
    );
}
export default DollarInput;
