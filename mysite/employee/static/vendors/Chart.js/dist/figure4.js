var figure = {
    "data": [
        {
            "uid": "48f87570-a580-11e8-b430-0242ac130002",
            "fill": "toself",
            "line": {
                "color": "#63AF63"
            },
            "meta": {
                "columnNames": {
                    "r": "Good Loans, r",
                    "theta": "Good Loans, theta"
                }
            },
            "mode": "lines+markers",
            "name": "Good Loans",
            "rsrc": "SNAT:22:85914c",
            "r": [
                13.27,
                12.95,
                12.44,
                13.98
            ],
            "type": "scatterpolar",
            "marker": {
                "size": 8,
                "color": "#B3FFB3",
                "symbol": "square"
            },
            "subplot": "polar",
            "thetasrc": "SNAT:22:85623c",
            "theta": [
                "Fully Paid",
                "Current",
                "Issued",
                "No C.P. Fully Paid"
            ]
        },
        {
            "uid": "48f87796-a580-11e8-b430-0242ac130002",
            "fill": "toself",
            "line": {
                "color": "#C31414"
            },
            "meta": {
                "columnNames": {
                    "r": "Bad Loans, r",
                    "theta": "Bad Loans, theta"
                }
            },
            "mode": "lines+markers",
            "name": "Bad Loans",
            "rsrc": "SNAT:22:8c0061",
            "r": [
                16.14,
                16.02,
                14.6,
                15.35,
                15.7,
                16
            ],
            "type": "scatterpolar",
            "marker": {
                "size": 8,
                "color": "#FF5050",
                "symbol": "square"
            },
            "subplot": "polar2",
            "thetasrc": "SNAT:22:fbb27a",
            "theta": [
                "Default Rate",
                "Charged Off",
                "C.P. Charged Off",
                "In Grace Period",
                "Late (16-30 days)",
                "Late (31-120 days)"
            ]
        }
    ],
    "layout": {
        "polar": {
            "domain": {
                "x": [
                    0,
                    0.4
                ],
                "y": [
                    0,
                    1
                ]
            },
            "radialaxis": {
                "type": "linear",
                "range": [
                    0,
                    14.735675675675676
                ],
                "tickfont": {
                    "size": 8
                },
                "autorange": true
            },
            "angularaxis": {
                "type": "category",
                "rotation": 90,
                "tickfont": {
                    "size": 8
                },
                "direction": "counterclockwise"
            }
        },
        "title": {
            "text": "Average Interest Rates <br> Loan Status Distribution"
        },
        "polar2": {
            "domain": {
                "x": [
                    0.6,
                    1
                ],
                "y": [
                    0,
                    1
                ]
            },
            "radialaxis": {
                "type": "linear",
                "range": [
                    0,
                    17.012432432432433
                ],
                "tickfont": {
                    "size": 8
                },
                "autorange": true
            },
            "angularaxis": {
                "type": "category",
                "rotation": 90,
                "tickfont": {
                    "size": 8
                },
                "direction": "clockwise"
            }
        },
        "autosize": true,
        "showlegend": false,
        "paper_bgcolor": "rgb(255, 248, 243)"
    },
    "frames": []
}