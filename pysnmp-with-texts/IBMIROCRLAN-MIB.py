#
# PySNMP MIB module IBMIROCRLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMIROCRLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, TimeTicks, Counter64, Unsigned32, Counter32, MibIdentifier, enterprises, ModuleIdentity, IpAddress, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "TimeTicks", "Counter64", "Unsigned32", "Counter32", "MibIdentifier", "enterprises", "ModuleIdentity", "IpAddress", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ibmIROCroutingRlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm2210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 72))
ibmIROC = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119))
ibmIROCrouting = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4))
ibmRlanTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 0))
ibmRlanMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1))
ibmRlanDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 2))
ibmRlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3))
ibmRlanGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 1))
rlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1))
rlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2))
class NBNames(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class IpxNetworkNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class IpxNodeNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class CircuitState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("closed", 1), ("listen", 2), ("reqSent", 3), ("ackRcvd", 4), ("ackSent", 5), ("open", 6), ("termSent", 7), ("dhcpWait", 8))

class ZeroOrigCounter32(Counter32):
    pass

rlanActiveUserTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2), )
if mibBuilder.loadTexts: rlanActiveUserTable.setStatus('mandatory')
rlanActiveUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlanActiveUserEntry.setStatus('mandatory')
rlanActiveUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserName.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserName.setDescription('could be null.')
rlanActiveUserConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserConnected.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserConnected.setDescription('The elapsed time since the connection opened.')
rlanActiveUserTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserTimeRemaining.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserTimeRemaining.setDescription('The amount of time the connection allowed. Zero means no limits.')
rlanActiveUserInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 4), ZeroOrigCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserInPkts.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserInPkts.setDescription('Packets for this user, starting with zero.')
rlanActiveUserOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 5), ZeroOrigCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserOutPkts.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserOutPkts.setDescription('Packets for this user, starting with zero.')
rlanActiveUserInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 6), ZeroOrigCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserInOctets.setDescription('Octets for this user, starting with zero.')
rlanActiveUserOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 7), ZeroOrigCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserOutOctets.setDescription('Octets for this user, starting with zero.')
rlanActiveUserActiveVC = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveUserActiveVC.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveUserActiveVC.setDescription('The connection is an active virtual connection.')
rlanActiveIpUserTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3), )
if mibBuilder.loadTexts: rlanActiveIpUserTable.setStatus('mandatory')
rlanActiveIpUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlanActiveIpUserEntry.setStatus('mandatory')
rlanActiveIpUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 1), CircuitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpUserState.setStatus('mandatory')
rlanActiveIpUserPrevState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 2), CircuitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpUserPrevState.setStatus('mandatory')
rlanActiveIpUserLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpUserLocalAddr.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveIpUserLocalAddr.setDescription('Ip address at this end of the interface.')
rlanActiveIpUserRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpUserRemoteAddr.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveIpUserRemoteAddr.setDescription('Ip address of the remote end of this interface.')
rlanActiveIpUserRemoteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpUserRemoteMask.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveIpUserRemoteMask.setDescription('Ip address mask of the remote end of this interface.')
rlanActiveIpUserRemoteName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpUserRemoteName.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveIpUserRemoteName.setDescription('The host name used be the remote box for Domain Name Server function.')
rlanActiveNBUserTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4), )
if mibBuilder.loadTexts: rlanActiveNBUserTable.setStatus('mandatory')
rlanActiveNBUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlanActiveNBUserEntry.setStatus('mandatory')
rlanActiveNBUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 1), CircuitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserState.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveNBUserState.setDescription('The state information may not be reliable, if the protocol type is notApplicable or negotiating.')
rlanActiveNBUserPrevState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 2), CircuitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserPrevState.setStatus('mandatory')
if mibBuilder.loadTexts: rlanActiveNBUserPrevState.setDescription('The state information may not be reliable, if the protocol type is notApplicable or negotiating.')
rlanActiveNBProtType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("negotiating", 2), ("nbContlProt", 3), ("nbFrameCntlProt", 4), ("bridgeProt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBProtType.setStatus('mandatory')
rlanActiveNBUserLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserLocalMac.setStatus('mandatory')
rlanActiveNBUserRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserRemoteMac.setStatus('mandatory')
rlanActiveNBUserRemoteNames = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 6), NBNames()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserRemoteNames.setStatus('mandatory')
rlanActiveNBUserRemoteClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserRemoteClass.setStatus('mandatory')
rlanActiveNBUserRemoteVerMaj = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserRemoteVerMaj.setStatus('mandatory')
rlanActiveNBUserRemoteVerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveNBUserRemoteVerMin.setStatus('mandatory')
rlanActiveIpxUserTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5), )
if mibBuilder.loadTexts: rlanActiveIpxUserTable.setStatus('mandatory')
rlanActiveIpxUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlanActiveIpxUserEntry.setStatus('mandatory')
rlanActiveIpxUserState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 1), CircuitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpxUserState.setStatus('mandatory')
rlanActiveIpxUserPrevState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 2), CircuitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpxUserPrevState.setStatus('mandatory')
rlanActiveIpxUserNetworkNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 3), IpxNetworkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpxUserNetworkNum.setStatus('mandatory')
rlanActiveIpxUserLocalNodeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 4), IpxNodeNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpxUserLocalNodeNum.setStatus('mandatory')
rlanActiveIpxUserRemoteNodeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 1, 5, 1, 5), IpxNodeNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlanActiveIpxUserRemoteNodeNum.setStatus('mandatory')
rlanActiveUserGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 1))
rlanActiveIpUserGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 2))
rlanActiveNBUserGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 3))
rlanActiveIpxUserGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 2, 4))
rlanCoreCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 1))
rlanIpCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 2))
rlanNBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 3))
rlanIpxCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 5, 3, 1, 4))
mibBuilder.exportSymbols("IBMIROCRLAN-MIB", rlanActiveIpxUserNetworkNum=rlanActiveIpxUserNetworkNum, rlanActiveIpUserRemoteName=rlanActiveIpUserRemoteName, ibmIROCrouting=ibmIROCrouting, rlanIpCompliance=rlanIpCompliance, rlanActiveNBUserGroup=rlanActiveNBUserGroup, ibmIROC=ibmIROC, rlanActiveUserInOctets=rlanActiveUserInOctets, ibmRlanGeneral=ibmRlanGeneral, rlanActiveIpxUserTable=rlanActiveIpxUserTable, rlanActiveIpUserEntry=rlanActiveIpUserEntry, IpxNetworkNumber=IpxNetworkNumber, rlanActiveIpUserState=rlanActiveIpUserState, rlanActiveIpxUserGroup=rlanActiveIpxUserGroup, MacAddress=MacAddress, rlanIpxCompliance=rlanIpxCompliance, rlanActiveUserConnected=rlanActiveUserConnected, IpxNodeNumber=IpxNodeNumber, ibmRlanMIB=ibmRlanMIB, rlanActiveNBUserPrevState=rlanActiveNBUserPrevState, rlanActiveIpUserRemoteMask=rlanActiveIpUserRemoteMask, rlanActiveIpxUserPrevState=rlanActiveIpxUserPrevState, rlanActiveNBUserRemoteMac=rlanActiveNBUserRemoteMac, ibm=ibm, rlanGroups=rlanGroups, ibmProd=ibmProd, rlanActiveUserName=rlanActiveUserName, rlanActiveIpUserGroup=rlanActiveIpUserGroup, rlanActiveNBUserRemoteVerMaj=rlanActiveNBUserRemoteVerMaj, rlanActiveIpUserRemoteAddr=rlanActiveIpUserRemoteAddr, rlanActiveIpxUserRemoteNodeNum=rlanActiveIpxUserRemoteNodeNum, rlanActiveIpUserLocalAddr=rlanActiveIpUserLocalAddr, rlanActiveUserInPkts=rlanActiveUserInPkts, rlanActiveNBUserEntry=rlanActiveNBUserEntry, ibmRlanTraps=ibmRlanTraps, rlanActiveUserOutPkts=rlanActiveUserOutPkts, rlanActiveUserTable=rlanActiveUserTable, rlanActiveIpUserPrevState=rlanActiveIpUserPrevState, rlanActiveNBUserRemoteClass=rlanActiveNBUserRemoteClass, rlanActiveUserOutOctets=rlanActiveUserOutOctets, rlanActiveUserActiveVC=rlanActiveUserActiveVC, rlanActiveUserGroup=rlanActiveUserGroup, rlanActiveUserEntry=rlanActiveUserEntry, ibmRlanConformance=ibmRlanConformance, rlanActiveNBUserState=rlanActiveNBUserState, rlanActiveNBUserRemoteNames=rlanActiveNBUserRemoteNames, rlanCoreCompliance=rlanCoreCompliance, rlanActiveNBProtType=rlanActiveNBProtType, ibmRlanDomains=ibmRlanDomains, rlanActiveIpxUserState=rlanActiveIpxUserState, rlanActiveIpxUserLocalNodeNum=rlanActiveIpxUserLocalNodeNum, ZeroOrigCounter32=ZeroOrigCounter32, rlanActiveNBUserRemoteVerMin=rlanActiveNBUserRemoteVerMin, ibmIROCroutingRlan=ibmIROCroutingRlan, rlanCompliances=rlanCompliances, rlanActiveUserTimeRemaining=rlanActiveUserTimeRemaining, NBNames=NBNames, rlanActiveNBUserTable=rlanActiveNBUserTable, CircuitState=CircuitState, rlanActiveIpUserTable=rlanActiveIpUserTable, rlanNBCompliance=rlanNBCompliance, rlanActiveIpxUserEntry=rlanActiveIpxUserEntry, rlanActiveNBUserLocalMac=rlanActiveNBUserLocalMac, ibm2210=ibm2210)
