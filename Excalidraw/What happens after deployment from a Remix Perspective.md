---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Deployed 
Smart Contract ^N1m9NZGu

1. EOA Deploys ^ZnbeVnzC

Metamask ^S9YrsDH6

Deployed 
Smart Contract ^AfuSlbyf

Metamask ^8z4NFF5b

2. EOA Calls ^bsdf1qSf

AAVE Pool
Smart Contract ^U1eji0gM

Infographic that represents:

1. An EOA deploying a smart contract that gets a flashloan, and repays it with interest.
2. The EOA that deployed the smart contract then calls the smart contract that was deployed:
    - The EOA calls the function 'fn_RequestFlashLoan' that is in the deployed smart contract (flashloan_request).
    - This function takes in two inputs, the token_address for the token that the caller wants to borrow, and the token_amount.
    - These inputs are then used to call the POOL.flashLoanSimple function which is a derived function. 

    - If the inputs are valid, and the smart contract has enough to pay for gas + the flashloan interest, the function call ^2w6GkDx6

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://excalidraw.com",
	"elements": [
		{
			"id": "FRWanBoEqt5P9gTgolxPD",
			"type": "ellipse",
			"x": 113.71717676246351,
			"y": 264.3636356843602,
			"width": 142.9375,
			"height": 148.5,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"seed": 1610403819,
			"version": 249,
			"versionNonce": 1067165867,
			"isDeleted": false,
			"boundElements": [],
			"updated": 1677656607812,
			"link": null,
			"locked": false
		},
		{
			"id": "N1m9NZGu",
			"type": "text",
			"x": 109.70155176246351,
			"y": 205.3206669343602,
			"width": 158,
			"height": 50,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": null,
			"seed": 2008193477,
			"version": 276,
			"versionNonce": 1473301381,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "y4MCGmUvXwJ5PwzRHxmSr",
					"type": "arrow"
				}
			],
			"updated": 1677656607812,
			"link": null,
			"locked": false,
			"text": "Deployed \nSmart Contract",
			"rawText": "Deployed \nSmart Contract",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 43,
			"containerId": null,
			"originalText": "Deployed \nSmart Contract"
		},
		{
			"type": "ellipse",
			"version": 240,
			"versionNonce": 18289381,
			"isDeleted": false,
			"id": "SOv5tmPc9TmUyrCbmFg7g",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 98.09998926246351,
			"y": -188.0816768156398,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 143,
			"height": 149,
			"seed": 1037822437,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "S9YrsDH6"
				},
				{
					"id": "y4MCGmUvXwJ5PwzRHxmSr",
					"type": "arrow"
				}
			],
			"updated": 1677656607812,
			"link": null,
			"locked": false
		},
		{
			"id": "S9YrsDH6",
			"type": "text",
			"x": 119.59998926246351,
			"y": -126.08167681563981,
			"width": 100,
			"height": 25,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": null,
			"seed": 681621227,
			"version": 97,
			"versionNonce": 230930923,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1677656607812,
			"link": null,
			"locked": false,
			"text": "Metamask",
			"rawText": "Metamask",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 18,
			"containerId": "SOv5tmPc9TmUyrCbmFg7g",
			"originalText": "Metamask"
		},
		{
			"type": "text",
			"version": 319,
			"versionNonce": 119219115,
			"isDeleted": false,
			"id": "ZnbeVnzC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 82.20703125,
			"y": -299.81640625,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 147,
			"height": 25,
			"seed": 1192152331,
			"groupIds": [],
			"roundness": null,
			"boundElements": null,
			"updated": 1677655764222,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "1. EOA Deploys",
			"rawText": "1. EOA Deploys",
			"baseline": 18,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1. EOA Deploys"
		},
		{
			"id": "y4MCGmUvXwJ5PwzRHxmSr",
			"type": "arrow",
			"x": 172.3851455124635,
			"y": -21.48402056563981,
			"width": 2.0859375,
			"height": 217.05078125,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"seed": 1127001675,
			"version": 160,
			"versionNonce": 2135613163,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1677656607823,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					2.0859375,
					217.05078125
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "SOv5tmPc9TmUyrCbmFg7g",
				"focus": -0.02657299005884745,
				"gap": 17.642628902519434
			},
			"endBinding": {
				"elementId": "N1m9NZGu",
				"focus": -0.1753713469739847,
				"gap": 9.75390625
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"type": "ellipse",
			"version": 304,
			"versionNonce": 2046909861,
			"isDeleted": false,
			"id": "AD_kXWC25wjgj9gy8f8ei",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 462.2484267624635,
			"y": 264.4437138093602,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 142.9375,
			"height": 148.5,
			"seed": 1706682597,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "4TzMz2_HOpSYiTnaOy5gZ",
					"type": "arrow"
				}
			],
			"updated": 1677656607812,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 329,
			"versionNonce": 1336959237,
			"isDeleted": false,
			"id": "AfuSlbyf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 458.2328017624635,
			"y": 205.4007450593602,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 158,
			"height": 50,
			"seed": 1507935211,
			"groupIds": [],
			"roundness": null,
			"boundElements": [
				{
					"id": "ZDeRwB9hDwHM6mTsdsCWj",
					"type": "arrow"
				}
			],
			"updated": 1677656607812,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Deployed \nSmart Contract",
			"rawText": "Deployed \nSmart Contract",
			"baseline": 43,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Deployed \nSmart Contract"
		},
		{
			"type": "ellipse",
			"version": 294,
			"versionNonce": 1399322725,
			"isDeleted": false,
			"id": "se4bH4MT0A1bv2Yff78-6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 446.6312392624635,
			"y": -188.0015986906398,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 143,
			"height": 149,
			"seed": 582321221,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "ZDeRwB9hDwHM6mTsdsCWj",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "8z4NFF5b"
				}
			],
			"updated": 1677656607812,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 150,
			"versionNonce": 1904077931,
			"isDeleted": false,
			"id": "8z4NFF5b",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 468.1312392624635,
			"y": -126.00159869063981,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 100,
			"height": 25,
			"seed": 814190219,
			"groupIds": [],
			"roundness": null,
			"boundElements": null,
			"updated": 1677656607812,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Metamask",
			"rawText": "Metamask",
			"baseline": 18,
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "se4bH4MT0A1bv2Yff78-6",
			"originalText": "Metamask"
		},
		{
			"type": "text",
			"version": 377,
			"versionNonce": 763246661,
			"isDeleted": false,
			"id": "bsdf1qSf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 431.14453125,
			"y": -299.736328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 130,
			"height": 25,
			"seed": 677819301,
			"groupIds": [],
			"roundness": null,
			"boundElements": null,
			"updated": 1677655758657,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "2. EOA Calls",
			"rawText": "2. EOA Calls",
			"baseline": 18,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "2. EOA Calls"
		},
		{
			"type": "arrow",
			"version": 267,
			"versionNonce": 1275447691,
			"isDeleted": false,
			"id": "ZDeRwB9hDwHM6mTsdsCWj",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 520.9163955124635,
			"y": -21.40394244063981,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 2.0859375,
			"height": 217.05078125,
			"seed": 2102101291,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"boundElements": null,
			"updated": 1677656607823,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "se4bH4MT0A1bv2Yff78-6",
				"focus": -0.02657299005884745,
				"gap": 17.642628902519434
			},
			"endBinding": {
				"elementId": "AfuSlbyf",
				"focus": -0.1753713469739847,
				"gap": 9.75390625
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					2.0859375,
					217.05078125
				]
			]
		},
		{
			"type": "ellipse",
			"version": 479,
			"versionNonce": 913761061,
			"isDeleted": false,
			"id": "DSWcoHPYS6ABNJuUcKBOX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 473.4954739659721,
			"y": 617.6184032120946,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 142.9375,
			"height": 148.5,
			"seed": 1987277163,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "4TzMz2_HOpSYiTnaOy5gZ",
					"type": "arrow"
				}
			],
			"updated": 1677656607812,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 536,
			"versionNonce": 1046034053,
			"isDeleted": false,
			"id": "U1eji0gM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 469.4798489659721,
			"y": 558.5754344620946,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 158,
			"height": 50,
			"seed": 1908862661,
			"groupIds": [],
			"roundness": null,
			"boundElements": null,
			"updated": 1677656607812,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "AAVE Pool\nSmart Contract",
			"rawText": "AAVE Pool\nSmart Contract",
			"baseline": 43,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "AAVE Pool\nSmart Contract"
		},
		{
			"id": "4TzMz2_HOpSYiTnaOy5gZ",
			"type": "arrow",
			"x": 548.209165042094,
			"y": 418.1545795560996,
			"width": 0.41461277970574884,
			"height": 175.2839945945342,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": {
				"type": 2
			},
			"seed": 331930507,
			"version": 338,
			"versionNonce": 592076843,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1677656607823,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.41461277970574884,
					175.2839945945342
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "AD_kXWC25wjgj9gy8f8ei",
				"focus": -0.20540304512406096,
				"gap": 6.615628306774212
			},
			"endBinding": {
				"elementId": "DSWcoHPYS6ABNJuUcKBOX",
				"focus": 0.036344511010213104,
				"gap": 24.2229003333251
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "2w6GkDx6",
			"type": "text",
			"x": -312.12716710812447,
			"y": -641.6272119819633,
			"width": 1838,
			"height": 320,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": null,
			"seed": 1348810699,
			"version": 1241,
			"versionNonce": 1320737067,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1677656610786,
			"link": null,
			"locked": false,
			"text": "Infographic that represents:\n\n1. An EOA deploying a smart contract that gets a flashloan, and repays it with interest.\n2. The EOA that deployed the smart contract then calls the smart contract that was deployed:\n    - The EOA calls the function 'fn_RequestFlashLoan' that is in the deployed smart contract (flashloan_request).\n    - This function takes in two inputs, the token_address for the token that the caller wants to borrow, and the token_amount.\n    - These inputs are then used to call the POOL.flashLoanSimple function which is a derived function. \n\n    - If the inputs are valid, and the smart contract has enough to pay for gas + the flashloan interest, the function call",
			"rawText": "Infographic that represents:\n\n1. An EOA deploying a smart contract that gets a flashloan, and repays it with interest.\n2. The EOA that deployed the smart contract then calls the smart contract that was deployed:\n    - The EOA calls the function 'fn_RequestFlashLoan' that is in the deployed smart contract (flashloan_request).\n    - This function takes in two inputs, the token_address for the token that the caller wants to borrow, and the token_amount.\n    - These inputs are then used to call the POOL.flashLoanSimple function which is a derived function. \n\n    - If the inputs are valid, and the smart contract has enough to pay for gas + the flashloan interest, the function call",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 309,
			"containerId": null,
			"originalText": "Infographic that represents:\n\n1. An EOA deploying a smart contract that gets a flashloan, and repays it with interest.\n2. The EOA that deployed the smart contract then calls the smart contract that was deployed:\n    - The EOA calls the function 'fn_RequestFlashLoan' that is in the deployed smart contract (flashloan_request).\n    - This function takes in two inputs, the token_address for the token that the caller wants to borrow, and the token_amount.\n    - These inputs are then used to call the POOL.flashLoanSimple function which is a derived function. \n\n    - If the inputs are valid, and the smart contract has enough to pay for gas + the flashloan interest, the function call"
		},
		{
			"id": "q46E32Aq",
			"type": "text",
			"x": 512.82421875,
			"y": 265.923828125,
			"width": 16,
			"height": 36,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": null,
			"seed": 611518315,
			"version": 25,
			"versionNonce": 297355,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1677656418844,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 25,
			"containerId": "AD_kXWC25wjgj9gy8f8ei",
			"originalText": ""
		},
		{
			"id": "5JpoxcM6",
			"type": "text",
			"x": 50.375,
			"y": -371.2421875,
			"width": 12,
			"height": 25,
			"angle": 0,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"roundness": null,
			"seed": 801251275,
			"version": 11,
			"versionNonce": 1109830405,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1677655762125,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 18,
			"containerId": null,
			"originalText": ""
		},
		{
			"type": "text",
			"version": 49,
			"versionNonce": 645185195,
			"isDeleted": true,
			"id": "yaz26ewi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 389.640625,
			"y": -372.06640625,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 12,
			"height": 25,
			"seed": 1906128709,
			"groupIds": [],
			"roundness": null,
			"boundElements": null,
			"updated": 1677655757088,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "",
			"rawText": "",
			"baseline": 18,
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": ""
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#000000",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "hachure",
		"currentItemStrokeWidth": 1,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 28,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 439.0899196630048,
		"scrollY": 758.4063727524637,
		"zoom": {
			"value": 0.6295830244815156
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"colorPalette": {},
		"currentStrokeOptions": null,
		"previousGridSize": null
	},
	"files": {}
}
```
%%