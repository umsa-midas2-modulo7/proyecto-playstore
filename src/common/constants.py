from typing import Final, List
from types.app import AppInfo, App

class AppConstants:
    
    APP_OBJ: Final[List[AppInfo]] = [
        {"app_id": "com.bancosol.altoke", "name": "Altoke"},
        {"app_id": "com.bcp.bo.wallet", "name": "Yape"},
        {"app_id": "bo.com.yolopago", "name": "YoloPago"}, 
        {"app_id": "com.busa.wallet", "name": "Yasta"},
        {"app_id": "com.walletapp.mobile", "name": "WalletApp"}
    ]

    APP_IDS: Final[List[str]] = [
        app["app_id"] for app in APP_OBJ
    ]
    
    APPS: Final[List[App]] = [
        App(app_id="com.bancosol.altoke", name="Altoke"),
        App(app_id="com.bcp.bo.wallet", name="Yape"),
        App(app_id="bo.com.yolopago", name="YoloPago"), 
        App(app_id="com.busa.wallet", name="Yasta"),
        App(app_id="com.walletapp.mobile", name="WalletApp")
    ]