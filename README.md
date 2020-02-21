# svarlr


The svarlr python package contains functions to estimate structural vector autoregressions with long-run restriction. It includes functions for estimating multivariate vector autoregressions with long-run restrictions imposed, generating impulse response functions, series bootstrapping and generating minimum distance confidence intervals. 

Thanks:

Dr. Xuan Liu (East Carolina University)

Dr. Jay Hong (University of Pennsylvania)

<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>svarlr_example</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="The-svarlr-Module">The <code>svarlr</code> Module<a class="anchor-link" href="#The-svarlr-Module">&#182;</a></h1><h5 id="Kyle-Murphy-2020-02-21">Kyle Murphy 2020-02-21<a class="anchor-link" href="#Kyle-Murphy-2020-02-21">&#182;</a></h5>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is a walkthrough of the svarlr package available here:</p>
<p><a href="https://pypi.org/project/svarlr/">https://pypi.org/project/svarlr/</a></p>
<p>The svarlr python package contains functions to estimate structural vector autoregressions with long-run restriction. It includes functions for estimating multivariate vector autoregressions with long-run restrictions imposed, generating impulse response filters, series bootstrapping and generating minimum distance confidence intervals.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The package can be installed with:</p>
<p><code>pip install svarlr</code></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Import the packages needed, in this case:</p>
<ul>
<li>numpy </li>
<li>pandas</li>
<li>matplotlib</li>
<li>svarlr</li>
<li>pandas-datareader (to download FRED data)</li>
<li>seaborn (better looking plots)</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># This is the proper way to install a package within a jupyter notebook </span>
<span class="c1"># environment.</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="o">!{</span>sys.executable<span class="o">}</span> -m pip install svarlr
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Requirement already satisfied: svarlr in /usr/local/lib/python3.7/site-packages (0.0.1)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span> 
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">svarlr</span>
<span class="kn">import</span> <span class="nn">pandas_datareader</span> <span class="k">as</span> <span class="nn">pdr</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>

<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="n">sns</span><span class="o">.</span><span class="n">set</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>/usr/local/lib/python3.7/site-packages/pandas_datareader/compat/__init__.py:7: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
  from pandas.util.testing import assert_frame_equal
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The data we are going to use is located here:</p>
<p><a href="https://raw.githubusercontent.com/murphy-k/svarlr/master/Germany.csv">https://raw.githubusercontent.com/murphy-k/svarlr/master/Germany.csv</a></p>
<p>Total Factor Productivity and Employment Total Hour Growth. We an explore how technology shocks impact employment, and vice-versa.</p>
<p>We can read in the data with the pandas module.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">series</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;https://raw.githubusercontent.com/murphy-k/svarlr/master/Germany.csv&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can index the data by the year column, and then drop it.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">series</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">series</span><span class="o">.</span><span class="n">Year</span>
<span class="n">series</span> <span class="o">=</span> <span class="n">series</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;Year&#39;</span><span class="p">],</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">series</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TFP</th>
      <th>TotHrGrowth</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1951-01-01</th>
      <td>6.894657</td>
      <td>1.037311</td>
    </tr>
    <tr>
      <th>1952-01-01</th>
      <td>5.080555</td>
      <td>0.634502</td>
    </tr>
    <tr>
      <th>1953-01-01</th>
      <td>4.542223</td>
      <td>1.454624</td>
    </tr>
    <tr>
      <th>1954-01-01</th>
      <td>3.185142</td>
      <td>1.806637</td>
    </tr>
    <tr>
      <th>1955-01-01</th>
      <td>5.412597</td>
      <td>2.032252</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2012-01-01</th>
      <td>-0.346423</td>
      <td>-0.127787</td>
    </tr>
    <tr>
      <th>2013-01-01</th>
      <td>-0.059366</td>
      <td>-0.288752</td>
    </tr>
    <tr>
      <th>2014-01-01</th>
      <td>0.591983</td>
      <td>1.158355</td>
    </tr>
    <tr>
      <th>2015-01-01</th>
      <td>0.423489</td>
      <td>1.006240</td>
    </tr>
    <tr>
      <th>2016-01-01</th>
      <td>0.804969</td>
      <td>0.616058</td>
    </tr>
  </tbody>
</table>
<p>66 rows × 2 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's define some variables before we begin model estimation. We need to specify the order of lag (we will use 1 in this example) as well as the number of periods for the Impulse Response Functions, and the maximum number of periods that we will show in the IRF graph.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p</span> <span class="o">=</span> <span class="mi">1</span>       <span class="c1"># order of VAR lag</span>
<span class="n">nIR</span> <span class="o">=</span> <span class="mi">50</span>    <span class="c1"># number of periods for Impulse Response</span>
<span class="n">nIRF</span> <span class="o">=</span> <span class="mi">5</span>    <span class="c1"># maximum periods shown in IRF graph</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The function <code>varlr</code> takes a series that can be an array or dataframe (will automatically be transformed to an array) that is our data. The second parameter is the VAR order, and is set to 1 by default.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">[</span><span class="n">b</span><span class="p">,</span> <span class="n">Sig</span><span class="p">,</span> <span class="n">B</span><span class="p">]</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">varlr</span><span class="p">(</span><span class="n">series</span><span class="p">,</span><span class="n">p</span><span class="p">)</span> <span class="c1"># VAR of order &#39;p&#39;</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><code>varlr</code> returns three objects:</p>
<ul>
<li>b: An array that is the VAR coefficient vector [A0,A1,...,Ap].</li>
<li>Sig: variance-covariance matrix of reduced form error.</li>
<li>B: structural transform matrix computed with long-run restriction imposed. [Blanchard-Quah (1989)].</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <code>irflr</code> function takes three arguments:</p>
<ul>
<li>b: The above estimated VAR coefficients.</li>
<li>B: The structural matrix for error.</li>
<li>nIR: The number of periods of the IRF.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">IRF</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">irflr</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="n">B</span><span class="p">,</span><span class="n">nIR</span><span class="p">)</span> <span class="c1"># Impulse response (or MA coefficients)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><code>irflr</code> returns an array.</p>
<p>$s-th$ column has $(s-1)$ period of IRF</p>
<p>$[ t(11) t(21) ... t(n1) t(12)...]'$</p>
<p>$t(ij)$ stands for effect of $j$ shock on variable $i$.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><code>cor</code> takes the impulse response of VAR and returns an array of correlation coefficients.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">corr</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">cor</span><span class="p">(</span><span class="n">IRF</span><span class="p">)</span> <span class="c1"># Correlations</span>
<span class="nb">print</span><span class="p">(</span><span class="n">corr</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[[ 0.22531014 -0.05921974  0.74241692]]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In order to get the impulse response of TFP, we need to some all the coefficients of dTFP. Then we can transform the array into a dataframe.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">IRF</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">vstack</span><span class="p">([(</span><span class="n">IRF</span><span class="p">[</span><span class="mi">0</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()),</span>
                 <span class="p">(</span><span class="n">IRF</span><span class="p">[</span><span class="mi">1</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()),</span>
                 <span class="p">(</span><span class="n">IRF</span><span class="p">[</span><span class="mi">2</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()),</span>
                 <span class="p">(</span><span class="n">IRF</span><span class="p">[</span><span class="mi">3</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">())])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We now have the impulse response functions, but we need to bootstrap the series to estalish confidence intervals.</p>
<p>First we can create objects to hold the various results from the loop we will implement to accompish the boostrapping.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Sim</span> <span class="o">=</span> <span class="mi">1000</span> <span class="c1"># The number of bootstrap iterations</span>

<span class="n">corr_b</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">IRF1</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">IRF2</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">IRF3</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">IRF4</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">srrsim</span> <span class="o">=</span> <span class="p">[]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><code>bootstrap</code> takes three arguments:</p>
<ul>
<li>y: The series to bootstrap.</li>
<li>p: The order of lags.</li>
<li>k: The number of initial observation trimming.</li>
</ul>
<p>And returns a bootstrapped series.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">Sim</span><span class="o">+</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">series_b</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">bootstrap</span><span class="p">(</span><span class="n">series</span><span class="p">,</span><span class="n">p</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">series</span><span class="p">)</span><span class="o">+</span><span class="mi">30</span><span class="p">)</span> <span class="c1"># Pseudo Series generated</span>
    <span class="n">b_b</span><span class="p">,</span><span class="n">Sig_b</span><span class="p">,</span><span class="n">B_b</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">varlr</span><span class="p">(</span><span class="n">series_b</span><span class="p">,</span> <span class="n">p</span><span class="p">)</span>
    <span class="n">IRF_b</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">irflr</span><span class="p">(</span><span class="n">b_b</span><span class="p">,</span><span class="n">B_b</span><span class="p">,</span><span class="n">nIR</span><span class="p">)</span>
    <span class="n">ith_cor</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">cor</span><span class="p">(</span><span class="n">IRF_b</span><span class="p">)</span>
    <span class="n">IRF1</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">IRF_b</span><span class="p">[</span><span class="mi">0</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()[</span><span class="n">np</span><span class="o">.</span><span class="n">newaxis</span><span class="p">])</span>
    <span class="n">IRF2</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">IRF_b</span><span class="p">[</span><span class="mi">1</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()[</span><span class="n">np</span><span class="o">.</span><span class="n">newaxis</span><span class="p">])</span>
    <span class="n">IRF3</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">IRF_b</span><span class="p">[</span><span class="mi">2</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()[</span><span class="n">np</span><span class="o">.</span><span class="n">newaxis</span><span class="p">])</span>
    <span class="n">IRF4</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">IRF_b</span><span class="p">[</span><span class="mi">3</span><span class="p">,:]</span><span class="o">.</span><span class="n">cumsum</span><span class="p">()[</span><span class="n">np</span><span class="o">.</span><span class="n">newaxis</span><span class="p">])</span>

<span class="n">IRF1</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">vstack</span><span class="p">(</span><span class="n">IRF1</span><span class="p">)</span>
<span class="n">IRF2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">vstack</span><span class="p">(</span><span class="n">IRF2</span><span class="p">)</span>
<span class="n">IRF3</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">vstack</span><span class="p">(</span><span class="n">IRF3</span><span class="p">)</span>
<span class="n">IRF4</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">vstack</span><span class="p">(</span><span class="n">IRF4</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <code>band</code> function calculates a minimum-distance interval and takes two arguments:</p>
<ul>
<li>mat: The array to calculate the intervals.</li>
<li>ptg: Decimal representation of confidence interval percentage.</li>
</ul>
<p>And returns the confidence intervals.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">band1</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">band</span><span class="p">(</span><span class="n">IRF1</span><span class="p">,</span><span class="o">.</span><span class="mi">90</span><span class="p">);</span>
<span class="n">band2</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">band</span><span class="p">(</span><span class="n">IRF2</span><span class="p">,</span><span class="o">.</span><span class="mi">90</span><span class="p">);</span>
<span class="n">band3</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">band</span><span class="p">(</span><span class="n">IRF3</span><span class="p">,</span><span class="o">.</span><span class="mi">90</span><span class="p">);</span>
<span class="n">band4</span> <span class="o">=</span> <span class="n">svarlr</span><span class="o">.</span><span class="n">band</span><span class="p">(</span><span class="n">IRF4</span><span class="p">,</span><span class="o">.</span><span class="mi">90</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can take all the above and put it together into a large plot with four subplots.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_IRF</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">IRF</span><span class="p">)</span>

<span class="c1"># First transpose the df. </span>
<span class="n">df_IRF</span> <span class="o">=</span> <span class="n">df_IRF</span><span class="o">.</span><span class="n">T</span>
<span class="n">col_names</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TFP &lt;- Technology Shock&#39;</span><span class="p">,</span> <span class="s1">&#39;Hours &lt;- Technology Shock&#39;</span><span class="p">,</span><span class="s1">&#39;Hours &lt;- Non-Technology Shock&#39;</span><span class="p">,</span><span class="s1">&#39;TFP &lt;- Non-Technology Shock&#39;</span><span class="p">]</span>
<span class="n">df_IRF</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="n">col_names</span>

<span class="c1"># Define graphic settings</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">nIRF</span><span class="o">+</span><span class="mi">1</span>
<span class="n">fig_size</span> <span class="o">=</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="mi">8</span><span class="p">)</span>
<span class="n">fig_dpi</span> <span class="o">=</span> <span class="mi">100</span> 

<span class="c1"># Build the plots</span>
<span class="n">fig</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span><span class="n">ncols</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="n">fig_size</span><span class="p">,</span> <span class="n">dpi</span><span class="o">=</span><span class="n">fig_dpi</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">suptitle</span><span class="p">(</span><span class="s2">&quot;IRF: Germany</span><span class="se">\n</span><span class="s2">Bootstrap-N: </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">Sim</span><span class="p">))</span>

<span class="c1"># First Plot</span>
<span class="n">df_IRF</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:</span><span class="n">t</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">);</span> <span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;TFP &lt;- Technology Shock&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">band1</span><span class="o">.</span><span class="n">T</span><span class="p">[:</span><span class="n">t</span><span class="p">,:],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dotted&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">([</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">]),</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dashed&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">fill_between</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="n">band1</span><span class="p">[</span><span class="mi">0</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span> <span class="n">band1</span><span class="p">[</span><span class="mi">1</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>

<span class="c1"># Second Plot</span>
<span class="n">df_IRF</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">);</span> <span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Hours &lt;- Technology Shock&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">band2</span><span class="o">.</span><span class="n">T</span><span class="p">[:</span><span class="n">t</span><span class="p">,:],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dotted&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">([</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">]),</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dashed&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">fill_between</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="n">band2</span><span class="p">[</span><span class="mi">0</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span> <span class="n">band2</span><span class="p">[</span><span class="mi">1</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
               
<span class="c1"># Third Plot</span>
<span class="n">df_IRF</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:</span><span class="n">t</span><span class="p">,</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">);</span> <span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Hours &lt;- Non-Technology Shock&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">band3</span><span class="o">.</span><span class="n">T</span><span class="p">[:</span><span class="n">t</span><span class="p">,:],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dotted&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">([</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">]),</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dashed&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">fill_between</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="n">band3</span><span class="p">[</span><span class="mi">0</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span> <span class="n">band3</span><span class="p">[</span><span class="mi">1</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>

<span class="c1"># Fouth Plot</span>
<span class="n">df_IRF</span><span class="o">.</span><span class="n">iloc</span><span class="p">[:</span><span class="n">t</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;black&#39;</span><span class="p">);</span> <span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;TFP &lt;- Non-Technology Shock&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">band4</span><span class="o">.</span><span class="n">T</span><span class="p">[:</span><span class="n">t</span><span class="p">,:],</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dotted&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">([</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">]),</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">linestyle</span><span class="o">=</span><span class="s1">&#39;dashed&#39;</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">fill_between</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="n">band4</span><span class="p">[</span><span class="mi">0</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span> <span class="n">band4</span><span class="p">[</span><span class="mi">1</span><span class="p">,:</span><span class="n">t</span><span class="p">],</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">,</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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DBnC5s2bqV69eqHHkTZW2lhpY4tJEQ/cmDFjlNatWxf63KxZs5SQkJBCf95///0CcWaz2f6TmZmpHDx4UOnatavSqFEjJTExsdBz3Lx5U2nSpInSsGFDZeLEicq5c+fua/1at26tjBkzpsD2s2fPKiEhIcqiRYsctk+bNk1p0KCBkp6erlgsFiUiIkIZMWKEQ8y8efOUbt26KWazWZk+fboSEhKi7N271/58XFycEhISonz77beKoijK3r17lZCQEGX27NkOx2nZsqUydOhQRVEUZdu2bUpISIiyefNmh5hZs2YpoaGhSlxcnKIoigOn350AACAASURBVNK8eXPlvffeUxRFUZYtW6aEhIQoR48eddhnzJgxSnh4uJKenq6cP39eCQkJUb7++muHmH79+ikhISHK9evXFUVRlKlTpyoNGzZUDAaDoiiKkp2drTz22GPKggULinppFUVRlE2bNilNmza1vy/Cw8OVV199tUA9ivM6TZkyRalfv75y7do1h31feuklpXnz5orNZlNOnDjhsE++IUOGKOPHj1cURVF69Oih9OvXT/n999+Vxx57TBk7dqxis9luWw8hijJmzJgi28H8n/w2Jr9dmTdvnsMx1q5dq4SEhCg7d+5UFCXvPf3SSy85xOzfv18JCQlR9u/fryiKoqxatUoJCQlR1q5da49JTExUQkJClPXr19u3ZWRkKB9//LFy5syZQssvbay0sdLGFp9cmi+jVq5cWeBn8ODBBeLq1atn/2nUqBG9e/fGZDIRHR1d5I1KKpXK/g3qdj2sVqsVi8Vi/7HZbPdUp/379wPQunVrh+NGRkaSk5PD4cOHiYuLIy0tjXbt2jnsO2jQIFatWoWT0/868Rs3bmz/vUqVKgBkZmY67PfXMVSVKlXCaDQCEBMTg1arLXCu5557DkVROHjwYIE6xMTEUL16dRo0aFBgH6PRyLFjx+z1fPrppx1iOnXq5PD4+eefJzs7m61btwKwZcsWcnNz6dy5c4Hz/lmHDh3YuXMnCxYsoH///tSqVYs9e/YwcuRI3nzzzQKXaW73OsXExNjHFf+1PgkJCVy8eJHDhw8D0LZtW4eYL7/8kg8++MD++OrVqwwcOBCVSsX777//8H9LF6XK39+/0HZw5cqVDm1bTEwMUPDz1alTJzQajf2ye0nUrVvX/nuFChWoXbs277//PmPG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69PT9e7dm+TkZEaMGMHq1asZPXp0vfMpdaVoKKkrzw15dRpJURRWrFjB8OHD6d69O4MHD2bmzJm4XC4tzZ133ql1OVVZv349GRkZrF+/HoBVq1aRmZnJ+++/z2WXXUbfvn3Zu3cvv/zyCw888AD9+vUjKyuLW2+9la+++qre+fv+++958MEHueqqq1i3bh2DBg1qVDlvvfVW0tLSmDhxYo3dTqcqLS1lxowZXHnllXTr1o3f/e53fPDBBwFphg4dyty5c3nppZe49NJL6d69O/feey8HDhxoVP5qoigKCxcu1LpKrr76alasWFEt3apVq7j++uvJyspiyJAhvPLKK3g8noA0X3zxBcOHD9eO8+GHH2rPfffdd2RkZPDDDz9w9913k5WVxeWXX87s2bNRFEVLV1lZyfz587n66qvp1q0bV199NW+88QaqqtZaBofDwbRp07jiiivo1q0bw4cPr9a153a7efnllxkwYABZWVmMHj2a1atXk5GRQW5uLp9//jkZGRl8//33AftVXYM//fRTjec+ceIEQI35e/DBB3nggQca9DoB5OXl8dRTTzFo0CC6d+/O73//e7788stq5XnllVcYOnQoWVlZDB8+nH/+85+1vkZfffUVXbt25bnnnqvztRQXl65duwJw5MiReqWXulLqSqkrg0sC0dN4vd4aH6d77rnntIpkwYIFjBgxguXLlzNmzJgGv9GKorB06VKmTZvG008/TVpaGvfffz9Op5OXX36Z119/nejoaB588EEOHjxY63GcTifvvfcev/vd77j77rupqKjg1Vdf5d///je33nprg18LAIvFwowZM8jNzeXll1+uNV1lZSV33HEHH330Effddx+vv/46vXv35i9/+QsLFy4MSLts2TL279/PjBkzmDp1Kj///DMTJkxoVP5q8uyzzzJ//nxuuOEGFi5cyLBhw5gyZQqLFi3S0rz99ts8/fTTZGVl8dprr3Hffffx1ltvMX36dC2Noig8//zz3HPPPSxcuJDExEQmTJhQbfzZ448/Tr9+/Vi0aBG/+c1vWLRokVYRqqrK6NGjWbp0KbfddpuWn1mzZvH888/XmH+n08ntt9/OJ598wujRo3n99dfp2bMnTz/9NEuWLNHSTZw4keXLl3PXXXcxb9487HY7zz33nPb84MGDiY+Pr1bRrVmzhvbt25OVlVXj+QcOHIjBYGDkyJG89tpr/PTTT1plmpWVxb333ovFYqn365Sfn8/NN9/Mli1bGD9+PPPmzaNFixY88MADrF27VjvOY489xttvv629Tv379+fJJ5/kk08+qZbHH374gXHjxnHDDTfw/PPPo9PpaiyLaJ5qqoN9Pl+99s3JyQEIaIU9ndSVflJX+kldGWSqUFVVVSdMmKCmp6fX+ZgwYYKqqqq6Z88eNT09XV20aFHAMdasWaOmp6erX375paqqqjpy5Eh15MiRAWl++OEHNT09Xf3hhx9UVVXVlStXqunp6eqaNWu0NPn5+Wp6err64YcfatscDoc6ffp0dffu3TXm//jx42p2drbas2dPdfLkyerevXvP+jVJT09X586dq6qqqs6YMUNNT09Xv/32W1VVVfXQoUNqenq6unLlSlVVVXXFihVqenq6+uOPPwYc45lnnlG7deumFhUVqaqqqkOGDFGHDBmier1eLc28efPU9PR0tbCwsN55GzJkiPZ+nKrqvXnjjTcCts+cOVPt3r27WlJSonq9XrVv377quHHjAtIsWrRIvemmm1SPx6POnj07oLyqqqr79u1T09PT1eXLl6uqqqrffvutmp6ers6bNy/gOIMGDVLHjBmjqqqq/vvf/1bT09PVTz75JCDN3Llz1YyMDHXfvn2qqqrqgAED1GeeeUZVVVVdtmyZmp6erv70008B+0yYMEHNyspSS0pK1P3796vp6enq22+/HZDmrrvuUtPT09Vjx46pqqqqL730ktqzZ0+1oqJCVVVVLS8vV3v06KEuWbKktpdWVVVVXbt2rdq/f3/t2s/KylLvu+++auWoz+s0Y8YMtVu3burRo0cD9h05cqQ6YMAA1efzqdu3bw/Yp8qDDz6oPvfcc6qqquptt92m3nXXXep///tftUePHupTTz2l+ny+Osshmp4JEyaoQ4YMqfG5uXPn1lr/Pvvss9XSeTwe7VFaWqpu3LhRvfHGG9XevXur+fn5NZ5D6ko/qSulrmwqpEX0FAkJCXzwwQc1Pk4d9L5hwwYArr322oD9r732WgwGg9bt3hCdO3fW/h8fH0+HDh149tlnmTBhAh999BE+n4+nn36ajh071ri/TqfTfunUNR5FUZRGtTI8+uijtG3bttZupw0bNpCSkkLPnj0Dtl933XW4XK6Aro1u3bphMBi0v6sGzjudTlRVrdYS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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We have now captured the linear interdependencies among multiple time series, in this case total factor productivity and total employment hour growth for Germany from 1951-2016.</p>
<p>Thank you.</p>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>
