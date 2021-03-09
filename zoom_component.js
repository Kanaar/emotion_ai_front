import { ZoomMtg } from '@zoomus/websdk';

ZoomMtg.preLoadWasm();
ZoomMtg.prepareJssdk();
// set web sdk lib path
ZoomMtg.setZoomJSLib('http://localhost:9999/custom/path/to/lib/', '/av')
// must be globally available
node_modules/@zoomus/websdk/dist/css/bootstrap.css
node_modules/@zoomus/websdk/dist/css/react-select.css
node_modules/jquery/dist/jquery.min.js

// configs
// setup your signautre endpoint here: https://github.com/zoom/websdk-sample-signature-node.js
var signatureEndpoint = 'http://localhost:4000'
var apiKey = 'JWT_API_KEY'
var meetingNumber = 123456789
var role = 0
var leaveUrl = 'http://localhost:9999'
var userName = 'WebSDK'
var userEmail = ''
var passWord = ''

// authenticate meeting signature
var signature = 'eHUzSlBhQV9SSlcyLTlsNV9IQWFMQS4xMjM0NTY3ODkuMTU4MzE2OTUzODc3My4wLkJMNEtiM3FINGx5ZzA1MUZtbGJOcGtPRnlFQS9lQUR2bGllVzJNNGZJeWs9'

// Init and join meeting
ZoomMtg.init({
  leaveUrl: leaveUrl,
  isSupportAV: true,
  success: (success) => {
    console.log(success)

    ZoomMtg.join({
      signature: signature,
      meetingNumber: meetingNumber,
      userName: userName,
      apiKey: apiKey,
      userEmail: userEmail,
      passWord: passWord,
      success: (success) => {
        console.log(success)
      },
      error: (error) => {
        console.log(error)
      }
    })

  },
  error: (error) => {
    console.log(error)
  }
})
