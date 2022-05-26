import {bindActionCreators} from 'redux';

import {store} from './Store';
import {isMobileChanged} from './slices/Global';


const _actions = bindActionCreators({
    isMobileChanged
}, store.dispatch);


export default function matchMedia() {
    const currentState = store.getState().global.isMobile;
    const isMobile = window.matchMedia('(max-width: 768px)').matches;

    if (currentState !== isMobile)
        _actions.isMobileChanged(isMobile);
}