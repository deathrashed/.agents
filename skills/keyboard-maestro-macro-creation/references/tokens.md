# Keyboard Maestro Tokens Reference

Full alphabetical list of KM tokens (from wiki.keyboardmaestro.com). Embed in text fields using `%TokenName%` syntax. Tokens are expanded at runtime.

## Clipboard
`%SystemClipboard%` `%CurrentClipboard%` `%NamedClipboard%` `%PastClipboard%` `%TriggerClipboard%`
`%SystemClipboardFlavors%` `%NamedClipboardFlavors%` `%PastClipboardFlavors%`
`%FindPasteboard%` `%PasteByNameText%`

## Application / Process
`%ApplicationName%` `%ApplicationPath%` `%ApplicationBundleID%` `%ApplicationVersion%` `%ApplicationLongVersion%`
`%CurrentApplication%` `%LastApplication%` `%LastWindowID%`

## Browsers
`%FrontBrowserTitle%` `%FrontBrowserURL%` `%FrontBrowserName%` `%FrontBrowserPath%` `%FrontBrowserBundleID%`
`%FrontBrowserJavaScript%` `%FrontBrowserField%` `%FrontBrowserVersion%`
`%SafariTitle%` `%SafariURL%` `%SafariJavaScript%` `%SafariField%`
`%ChromeTitle%` `%ChromeURL%` `%ChromeJavaScript%` `%ChromeField%`

## Date / Time
`%ICUDateTime%` `%ICUDateTimeFor%` `%ICUDateTimeMinus%` `%ICUDateTimePlus%`
`%ShortDate%` `%LongDate%` `%NumberDate%`
`%ShortTime%` `%LongTime%`

## System
`%MacIPAddress%` `%MacName%` `%MacUUID%`
`%SystemVersion%` `%SystemLongVersion%`
`%SystemVolume%` `%WirelessNetwork%` `%NetworkLocation%` `%KeyboardLayout%`

## Window / Screen
`%FrontWindowName%` `%FrontWindowFrame%` `%FrontWindowPosition%` `%FrontWindowSize%`
`%WindowName%` `%WindowFrame%` `%WindowPosition%` `%WindowSize%`
`%Screen%` `%ScreenResolution%` `%ScreenResolutions%` `%ScreenVisible%`
`%FrontDocumentPath%`

## Variables & Dictionaries
`%Variable%VariableName%` `%Dictionary%DictionaryName%`
`%JSONFromVariables%` `%JSONFromDictionary%` `%JSONValue%`
`%AccessedVariables%`
`%ExecutingMacro%` `%ExecutingMacroGroup%` `%ExecutingThisMacro%`

## Finder
`%FinderSelection%` `%FinderSelections%` `%FinderInsertionLocation%`

## Mail
`%MailSubject%` `%MailSender%` `%MailContents%` `%MailRawSource%`
`%MailRecipients%` `%MailCCRecipients%` `%MailBCCRecipients%`

## Music
`%CurrentTrack%` `%MusicPlayerState%`

## Utility
`%Calculate%expression%` `%CalculateFormat%format,expression%`
`%RandomUUID%` `%TriggerValue%` `%Trigger%` `%TriggerBase%`
`%ActionResult%` `%PromptButton%` `%PromptWithListText%` `%SelectMenuByNameText%`
`%FoundImage%` `%HTMLResult%`
`%AddressBook%` `%AlertButton%`
`%UserHome%` `%UserLoginID%` `%UserName%`

## Literal helpers
`%Return%` `%Tab%` `%Space%` `%LineFeed%` `%VBAR%` `%Delete%` `%Bin%`
`%Hex%` `%Dec%` `%Oct%` `%OptionReturn%`
