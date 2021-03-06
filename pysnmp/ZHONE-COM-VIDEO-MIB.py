#
# PySNMP MIB module ZHONE-COM-VIDEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-VIDEO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, ifPhysAddress = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifPhysAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Counter64, ModuleIdentity, ObjectIdentity, Unsigned32, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneVideo, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneVideo", "zhoneModules")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
comVideo = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 78))
comVideo.setRevisions(('2003-10-28 11:00',))
if mibBuilder.loadTexts: comVideo.setLastUpdated('200310281012Z')
if mibBuilder.loadTexts: comVideo.setOrganization('Zhone Technologies, Inc.')
videoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 8, 1)).setObjects(("ZHONE-COM-VIDEO-MIB", "videoInterfaceRowStatus"), ("ZHONE-COM-VIDEO-MIB", "videoInterfaceType"), ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceRowStatus"), ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceIpAddress"), ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceNetMask"), ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceIndexNext"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoGroup = videoGroup.setStatus('current')
videoInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 8, 2), )
if mibBuilder.loadTexts: videoInterfaceTable.setStatus('current')
videoInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 8, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: videoInterfaceEntry.setStatus('current')
videoInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 8, 2, 1, 1), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: videoInterfaceRowStatus.setStatus('current')
videoInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("management", 1), ("stream", 2), ("client", 3))).clone('management')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: videoInterfaceType.setStatus('current')
videoMulticastSourceTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 8, 3), )
if mibBuilder.loadTexts: videoMulticastSourceTable.setStatus('current')
videoMulticastSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1), ).setIndexNames((0, "ZHONE-COM-VIDEO-MIB", "videoMulticastSourceIndex"))
if mibBuilder.loadTexts: videoMulticastSourceEntry.setStatus('current')
videoMulticastSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: videoMulticastSourceIndex.setStatus('current')
videoMulticastSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 2), ZhoneRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoMulticastSourceRowStatus.setStatus('current')
videoMulticastSourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoMulticastSourceIpAddress.setStatus('current')
videoMulticastSourceNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: videoMulticastSourceNetMask.setStatus('current')
videoMulticastSourceIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoMulticastSourceIndexNext.setStatus('current')
mibBuilder.exportSymbols("ZHONE-COM-VIDEO-MIB", videoMulticastSourceIndexNext=videoMulticastSourceIndexNext, videoGroup=videoGroup, videoInterfaceEntry=videoInterfaceEntry, comVideo=comVideo, videoInterfaceType=videoInterfaceType, videoInterfaceTable=videoInterfaceTable, videoMulticastSourceTable=videoMulticastSourceTable, PYSNMP_MODULE_ID=comVideo, videoMulticastSourceNetMask=videoMulticastSourceNetMask, videoMulticastSourceIpAddress=videoMulticastSourceIpAddress, videoMulticastSourceRowStatus=videoMulticastSourceRowStatus, videoMulticastSourceEntry=videoMulticastSourceEntry, videoMulticastSourceIndex=videoMulticastSourceIndex, videoInterfaceRowStatus=videoInterfaceRowStatus)
