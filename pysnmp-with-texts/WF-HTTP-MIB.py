#
# PySNMP MIB module WF-HTTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WF-HTTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Counter32, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, TimeTicks, Bits, Gauge32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Counter32", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "TimeTicks", "Bits", "Gauge32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfHttpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfHttpGroup")
wfHttp = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1))
wfHttpSrv = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1))
wfHttpSrvDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2))).clone('create')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvDelete.setDescription('Set to delete this server instance.')
wfHttpSrvDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvDisable.setDescription('Used to enable/disable the server.')
wfHttpSrvState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSrvState.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvState.setDescription('Current state of the server entity.')
wfHttpSrvPort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvPort.setDescription('The port number this server listens to requests on.')
wfHttpSrvMaxCacheCount = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvMaxCacheCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvMaxCacheCount.setDescription('The maximum number of archives that will be cached in system RAM. Increasing this value will improve performance for multiple simultaneous request at the cost of memory utilization.')
wfHttpSrvMaxCacheAge = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvMaxCacheAge.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvMaxCacheAge.setDescription('The maximumtime in seconds that an archive will be cached in system RAM.')
wfHttpSrvAuthType = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basic", 1), ("digest", 2))).clone('basic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvAuthType.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvAuthType.setDescription('The authentication type to use when authorizating requests')
wfHttpSrvHostName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvHostName.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvHostName.setDescription("The fully qualified domain name used for the HTTP server. If the name is set it domain name service must also by provided to allow clients to resolve the name. If this parameter is not configured the IP address of one of the router's interface will be used as the host name.")
wfHttpSrvHelpBaseUrl = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 9), DisplayString().clone('http://support.baynetworks.com/library/tpubs/')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvHelpBaseUrl.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSrvHelpBaseUrl.setDescription('A url that is used in all BASE tags that reside in help pages. This base url combined with a relative url points to more detailed information too large for storage on the router.')
wfHttpStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2))
wfHttpSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1))
wfHttpSummaryRequests = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryRequests.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryRequests.setDescription('The total number of requests generated or received by this entity.')
wfHttpSummaryRequestErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryRequestErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryRequestErrors.setDescription('Total number of request errors detected by this entity (as server).')
wfHttpSummaryRequestDiscards = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryRequestDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryRequestDiscards.setDescription('Total number of requests discarded by this entity (as server).')
wfHttpSummaryResponses = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryResponses.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryResponses.setDescription('Total number of responses generated or received by this entity.')
wfHttpSummaryResponseErrors = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryResponseErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryResponseErrors.setDescription('Total number of response errors detected by this entity (as client).')
wfHttpSummaryResponseDiscards = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryResponseDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryResponseDiscards.setDescription('The total number of responses discarded by this entity (as client).')
wfHttpSummaryInUnknowns = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryInUnknowns.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryInUnknowns.setDescription('The total number of unknown messages received by this entity.')
wfHttpSummaryInBytes = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryInBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryInBytes.setDescription('The total number of bytes received by this entity.')
wfHttpSummaryOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryOutBytes.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryOutBytes.setDescription('The total number of bytes transmitted by this entity.')
wfHttpSummaryTimeOuts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryTimeOuts.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryTimeOuts.setDescription('The number of timeouts for this entity.')
wfHttpSummaryStartTime = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpSummaryStartTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpSummaryStartTime.setDescription('The value of sysUpTime at the time the server started.')
wfHttpRequestTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2), )
if mibBuilder.loadTexts: wfHttpRequestTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestTable.setDescription('Table providing detailed request statistics broken out by request type.')
wfHttpRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1), ).setIndexNames((0, "WF-HTTP-MIB", "wfHttpRequestMethodIndex"))
if mibBuilder.loadTexts: wfHttpRequestEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestEntry.setDescription('An entry in the request table.')
wfHttpRequestMethodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("get", 1), ("head", 2), ("trace", 3), ("post", 4), ("options", 5), ("put", 6), ("delete", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpRequestMethodIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestMethodIndex.setDescription('The request method that these statistics apply to.')
wfHttpRequestInCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpRequestInCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestInCount.setDescription('The number of requests of this type received by the entity.')
wfHttpRequestInLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpRequestInLastTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestInLastTime.setDescription('The value of sysUpTime at the time the last request was received.')
wfHttpRequestOutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpRequestOutCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestOutCount.setDescription('The number of requests of this type generated by this entity.')
wfHttpRequestOutLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpRequestOutLastTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpRequestOutLastTime.setDescription('The value of sysUpTime at the time the last request was generated.')
wfHttpResponseTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3), )
if mibBuilder.loadTexts: wfHttpResponseTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseTable.setDescription('Response table, providing break-out of responses by response type.')
wfHttpResponseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1), ).setIndexNames((0, "WF-HTTP-MIB", "wfHttpResponseStatusIndex"))
if mibBuilder.loadTexts: wfHttpResponseEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseEntry.setDescription('An entry in the response table.')
wfHttpResponseStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(200, 201, 202, 204, 301, 302, 304, 400, 401, 403, 404, 500, 501, 502, 503))).clone(namedValues=NamedValues(("ok", 200), ("created", 201), ("accepted", 202), ("no-content", 204), ("moved-permanently", 301), ("moved-temporarily", 302), ("not-modified", 304), ("bad-request", 400), ("unauthorized", 401), ("forbidden", 403), ("not-found", 404), ("internal-server-error", 500), ("not-implemented", 501), ("bad-gateway", 502), ("service-unavailable", 503)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpResponseStatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseStatusIndex.setDescription('The response code for this row of the table.')
wfHttpResponseInCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpResponseInCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseInCount.setDescription('The number of times this response was received.')
wfHttpResponseInLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpResponseInLastTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseInLastTime.setDescription('The value of sysUpTime when this response was last received.')
wfHttpResponseOutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpResponseOutCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseOutCount.setDescription('The number of times this response was generated.')
wfHttpResponseOutLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfHttpResponseOutLastTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfHttpResponseOutLastTime.setDescription('The value of sysUpTime when this response was last sent.')
mibBuilder.exportSymbols("WF-HTTP-MIB", wfHttpSummary=wfHttpSummary, wfHttp=wfHttp, wfHttpRequestTable=wfHttpRequestTable, wfHttpSrvHostName=wfHttpSrvHostName, wfHttpRequestOutCount=wfHttpRequestOutCount, wfHttpSummaryRequests=wfHttpSummaryRequests, wfHttpSrvDisable=wfHttpSrvDisable, wfHttpResponseTable=wfHttpResponseTable, wfHttpSrvHelpBaseUrl=wfHttpSrvHelpBaseUrl, wfHttpSummaryRequestDiscards=wfHttpSummaryRequestDiscards, wfHttpSummaryRequestErrors=wfHttpSummaryRequestErrors, wfHttpResponseStatusIndex=wfHttpResponseStatusIndex, wfHttpResponseInCount=wfHttpResponseInCount, wfHttpResponseEntry=wfHttpResponseEntry, wfHttpSrvMaxCacheCount=wfHttpSrvMaxCacheCount, wfHttpSrvPort=wfHttpSrvPort, wfHttpResponseOutCount=wfHttpResponseOutCount, wfHttpResponseOutLastTime=wfHttpResponseOutLastTime, wfHttpSummaryResponseErrors=wfHttpSummaryResponseErrors, wfHttpSummaryResponseDiscards=wfHttpSummaryResponseDiscards, wfHttpSrvAuthType=wfHttpSrvAuthType, wfHttpSummaryTimeOuts=wfHttpSummaryTimeOuts, wfHttpRequestOutLastTime=wfHttpRequestOutLastTime, wfHttpSrv=wfHttpSrv, wfHttpSrvState=wfHttpSrvState, wfHttpSummaryOutBytes=wfHttpSummaryOutBytes, wfHttpRequestInCount=wfHttpRequestInCount, wfHttpResponseInLastTime=wfHttpResponseInLastTime, wfHttpSummaryInBytes=wfHttpSummaryInBytes, wfHttpStatistics=wfHttpStatistics, wfHttpSrvDelete=wfHttpSrvDelete, wfHttpSummaryInUnknowns=wfHttpSummaryInUnknowns, wfHttpSrvMaxCacheAge=wfHttpSrvMaxCacheAge, wfHttpSummaryStartTime=wfHttpSummaryStartTime, wfHttpRequestEntry=wfHttpRequestEntry, wfHttpSummaryResponses=wfHttpSummaryResponses, wfHttpRequestMethodIndex=wfHttpRequestMethodIndex, wfHttpRequestInLastTime=wfHttpRequestInLastTime)