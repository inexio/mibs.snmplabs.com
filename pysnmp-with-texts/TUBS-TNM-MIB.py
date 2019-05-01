#
# PySNMP MIB module TUBS-TNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-TNM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Unsigned32, ObjectIdentity, ModuleIdentity, enterprises, Integer32, Counter32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "enterprises", "Integer32", "Counter32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "IpAddress", "iso")
DateAndTime, TAddress, DisplayString, RowStatus, TimeStamp, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TAddress", "DisplayString", "RowStatus", "TimeStamp", "TruthValue", "TextualConvention")
tnmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 1))
if mibBuilder.loadTexts: tnmMIB.setLastUpdated('9411152024Z')
if mibBuilder.loadTexts: tnmMIB.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: tnmMIB.setContactInfo(' Juergen Schoenwaelder Postal: TU Braunschweig Bueltenweg 74/75 D-38108 Braunschweig GERMANY Tel: +49 531 391 3249 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: tnmMIB.setDescription('Experimental MIB modules for tnm based agents.')
tnmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1))
tnmVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmVersion.setStatus('current')
if mibBuilder.loadTexts: tnmVersion.setDescription('The version number of the tnm agent.')
tnmTclVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmTclVersion.setStatus('current')
if mibBuilder.loadTexts: tnmTclVersion.setDescription('The version number of the running Tcl interpreter.')
tnmTclCmdCount = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmTclCmdCount.setStatus('current')
if mibBuilder.loadTexts: tnmTclCmdCount.setDescription('The nummber of Tcl statements evaluated so far.')
tnmDate = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmDate.setStatus('current')
if mibBuilder.loadTexts: tnmDate.setDescription('The current date.')
tnmTrapDst = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmTrapDst.setStatus('current')
if mibBuilder.loadTexts: tnmTrapDst.setDescription('The host name of the trap sink host.')
tnmTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmTrapMsg.setStatus('current')
if mibBuilder.loadTexts: tnmTrapMsg.setDescription('The description of the last trap create by this entity.')
tnmDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2))
class URL(TextualConvention, OctetString):
    description = 'A uniform ressource locator as defined in RFC 1738.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

tnmHttpProxy = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmHttpProxy.setStatus('current')
if mibBuilder.loadTexts: tnmHttpProxy.setDescription('This variable specifies the proxy server. It must be of the form <name>[:<port>] where <name> is either a domain name or an IP address and <port> is the port number used to access the proxy server. The default port number is 80.')
tnmHttpSource = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 2), URL()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmHttpSource.setStatus('current')
if mibBuilder.loadTexts: tnmHttpSource.setDescription('Setting this variable will make tnm to download and source the document with the given URL. The agent will try to retrieve the document and sets the variable to the URL if this operations was successfull. Otherwise, the value will become an empty string.')
tnmHttpError = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmHttpError.setStatus('current')
if mibBuilder.loadTexts: tnmHttpError.setDescription('This variable contains an error string is an http operation fails. An empty string signals that the last operation completed successfully.')
tnmPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3))
tnmPeerTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1), )
if mibBuilder.loadTexts: tnmPeerTable.setStatus('current')
if mibBuilder.loadTexts: tnmPeerTable.setDescription('A (conceptual) table storing known tnm peers.')
tnmPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1), ).setIndexNames((0, "TUBS-TNM-MIB", "tnmPeerTAddress"))
if mibBuilder.loadTexts: tnmPeerEntry.setStatus('current')
if mibBuilder.loadTexts: tnmPeerEntry.setDescription('An entry (conceptual row) in the peer table.')
tnmPeerTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 1), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerTAddress.setStatus('current')
if mibBuilder.loadTexts: tnmPeerTAddress.setDescription('The address and port number of the peer agent.')
tnmPeerAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerAuth.setStatus('current')
if mibBuilder.loadTexts: tnmPeerAuth.setDescription('The authentication information for this peer. This will usually be a community string until we get the final SNMPv2 decisions about the security model.')
tnmPeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerState.setStatus('current')
if mibBuilder.loadTexts: tnmPeerState.setDescription('The current status of the peer as returned by the last status probe message.')
tnmPeerLastChecked = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 4), TimeStamp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerLastChecked.setStatus('current')
if mibBuilder.loadTexts: tnmPeerLastChecked.setDescription('The value of sysUpTime when the status of the peer was retrieved and written to tnmPeerState.')
tnmPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 3, 1, 1, 5), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmPeerStatus.setStatus('current')
if mibBuilder.loadTexts: tnmPeerStatus.setDescription('The status column used for creating, modifying, and deleting instances of the columnar objects in the tnm peer table.')
tnmElection = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4))
tnmElectionIndex = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmElectionIndex.setStatus('current')
if mibBuilder.loadTexts: tnmElectionIndex.setDescription('The (hopefully) unique Index of this peer used by the Gully election algorithm.')
tnmElectionPanic = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmElectionPanic.setStatus('current')
if mibBuilder.loadTexts: tnmElectionPanic.setDescription('Reading this variable will start the panic algorithm on this peer. (We should use an inform request here.)')
tnmElectionMaster = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 4, 3), TAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnmElectionMaster.setStatus('current')
if mibBuilder.loadTexts: tnmElectionMaster.setDescription('This variable will be set by a new master appearing on the scene. (We should use an inform request here.)')
tnmEval = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5))
tnmEvalSlot = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmEvalSlot.setStatus('current')
if mibBuilder.loadTexts: tnmEvalSlot.setDescription('The index number of the first unassigned entry in the evaluation table. A management station should create new entries in the evaluation table using this algorithm: first, issue a management protocol retrieval operation to determine the value of evalSlot; and, second, issue a management protocol set operation to create an instance of the evalStatus object setting its value to underCreation(1). If this latter operation succeeds, then the management station may continue modifying the instances corresponding to the newly created conceptual row, without fear of collision with other management stations.')
tnmEvalTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2), )
if mibBuilder.loadTexts: tnmEvalTable.setStatus('current')
if mibBuilder.loadTexts: tnmEvalTable.setDescription('The (conceptual) evaluation table.')
tnmEvalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1), ).setIndexNames((0, "TUBS-TNM-MIB", "tnmEvalIndex"))
if mibBuilder.loadTexts: tnmEvalEntry.setStatus('current')
if mibBuilder.loadTexts: tnmEvalEntry.setDescription('An entry (conceptual row) in the evaluation table.')
tnmEvalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmEvalIndex.setStatus('current')
if mibBuilder.loadTexts: tnmEvalIndex.setDescription('The auxiliary variable used for identifying instances of the columnar objects in the evaluation table.')
tnmEvalString = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmEvalString.setStatus('current')
if mibBuilder.loadTexts: tnmEvalString.setDescription('The string to evaluate.')
tnmEvalValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnmEvalValue.setStatus('current')
if mibBuilder.loadTexts: tnmEvalValue.setDescription('The value resturned by executing evalString.')
tnmEvalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 1, 5, 2, 1, 4), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnmEvalStatus.setStatus('current')
if mibBuilder.loadTexts: tnmEvalStatus.setDescription('The status column used for creating, modifying, and deleting instances of the columnar objects in the evaluation table.')
mibBuilder.exportSymbols("TUBS-TNM-MIB", tnmEvalSlot=tnmEvalSlot, tnmDate=tnmDate, PYSNMP_MODULE_ID=tnmMIB, tnmTclCmdCount=tnmTclCmdCount, tnmPeerState=tnmPeerState, tnmElectionMaster=tnmElectionMaster, tnmPeerStatus=tnmPeerStatus, tnmPeerTAddress=tnmPeerTAddress, tnmMIB=tnmMIB, tnmHttpSource=tnmHttpSource, tnmHttpError=tnmHttpError, tnmEvalValue=tnmEvalValue, tnmEvalEntry=tnmEvalEntry, tnmVersion=tnmVersion, tnmTclVersion=tnmTclVersion, tnmPeers=tnmPeers, tnmStatus=tnmStatus, tnmTrapDst=tnmTrapDst, URL=URL, tnmEvalIndex=tnmEvalIndex, tnmPeerEntry=tnmPeerEntry, tnmElectionIndex=tnmElectionIndex, tnmPeerTable=tnmPeerTable, tnmTrapMsg=tnmTrapMsg, tnmPeerLastChecked=tnmPeerLastChecked, tnmEval=tnmEval, tnmEvalString=tnmEvalString, tnmEvalStatus=tnmEvalStatus, tnmElectionPanic=tnmElectionPanic, tnmEvalTable=tnmEvalTable, tnmElection=tnmElection, tnmPeerAuth=tnmPeerAuth, tnmHttpProxy=tnmHttpProxy, tnmDownload=tnmDownload)
