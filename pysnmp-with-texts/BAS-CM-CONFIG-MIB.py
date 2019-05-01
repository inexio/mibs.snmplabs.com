#
# PySNMP MIB module BAS-CM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-CM-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
basCmConfig, = mibBuilder.importSymbols("BAS-MIB", "basCmConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Bits, Unsigned32, iso, TimeTicks, NotificationType, ObjectIdentity, Gauge32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Bits", "Unsigned32", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "Gauge32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
basCmConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1))
if mibBuilder.loadTexts: basCmConfigMIB.setLastUpdated('9901200000Z')
if mibBuilder.loadTexts: basCmConfigMIB.setOrganization('Broadband Access Systems, Inc.')
if mibBuilder.loadTexts: basCmConfigMIB.setContactInfo(' Tech Support Broadband Access Systems, Inc. 201 Forest Street Marlborough, MA 01752 USA 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basCmConfigMIB.setDescription('This MIB module defines the configuration MIB objects used to create cable modem configuration files. ')
basCmDsFreq = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmDsFreq.setStatus('current')
if mibBuilder.loadTexts: basCmDsFreq.setDescription('The receive frequency to be used by the CM. It is an override for the channel selected during scanning. This is the center frequency of the downstream channel in Hz stored as a 32-bit binary number.')
basCmUsChannelId = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmUsChannelId.setStatus('current')
if mibBuilder.loadTexts: basCmUsChannelId.setDescription('')
basCmNetworkAccess = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmNetworkAccess.setStatus('current')
if mibBuilder.loadTexts: basCmNetworkAccess.setDescription('')
basCmCosTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4), )
if mibBuilder.loadTexts: basCmCosTable.setStatus('current')
if mibBuilder.loadTexts: basCmCosTable.setDescription('')
basCmCosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1), ).setIndexNames((0, "BAS-CM-CONFIG-MIB", "basCmCosClassId"))
if mibBuilder.loadTexts: basCmCosEntry.setStatus('current')
if mibBuilder.loadTexts: basCmCosEntry.setDescription('')
basCmCosClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosClassId.setStatus('current')
if mibBuilder.loadTexts: basCmCosClassId.setDescription('')
basCmCosMaxDsBps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosMaxDsBps.setStatus('current')
if mibBuilder.loadTexts: basCmCosMaxDsBps.setDescription('')
basCmCosMaxUsBps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosMaxUsBps.setStatus('current')
if mibBuilder.loadTexts: basCmCosMaxUsBps.setDescription('')
basCmCosUsPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("zero", 0), ("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosUsPriority.setStatus('current')
if mibBuilder.loadTexts: basCmCosUsPriority.setDescription('')
basCmCosGuaranteedUsBps = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosGuaranteedUsBps.setStatus('current')
if mibBuilder.loadTexts: basCmCosGuaranteedUsBps.setDescription('')
basCmCosMaxUsBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosMaxUsBurst.setStatus('current')
if mibBuilder.loadTexts: basCmCosMaxUsBurst.setDescription('')
basCmCosBp = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCosBp.setStatus('current')
if mibBuilder.loadTexts: basCmCosBp.setDescription('')
basCmCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 5))
basCmCapConcat = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmCapConcat.setStatus('current')
if mibBuilder.loadTexts: basCmCapConcat.setDescription('')
basSnmpMibObjectTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11), )
if mibBuilder.loadTexts: basSnmpMibObjectTable.setStatus('current')
if mibBuilder.loadTexts: basSnmpMibObjectTable.setDescription('')
basSnmpMibObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11, 1), ).setIndexNames((0, "BAS-CM-CONFIG-MIB", "basSnmpMibObjectIdx"))
if mibBuilder.loadTexts: basSnmpMibObjectEntry.setStatus('current')
if mibBuilder.loadTexts: basSnmpMibObjectEntry.setDescription('')
basSnmpMibObjectIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSnmpMibObjectIdx.setStatus('current')
if mibBuilder.loadTexts: basSnmpMibObjectIdx.setDescription('')
basSnmpMibObjectVarBind = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basSnmpMibObjectVarBind.setStatus('current')
if mibBuilder.loadTexts: basSnmpMibObjectVarBind.setDescription('')
basCpeAddressTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14), )
if mibBuilder.loadTexts: basCpeAddressTable.setStatus('current')
if mibBuilder.loadTexts: basCpeAddressTable.setDescription('')
basCpeAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14, 1), ).setIndexNames((0, "BAS-CM-CONFIG-MIB", "basCpeAddressIdx"))
if mibBuilder.loadTexts: basCpeAddressEntry.setStatus('current')
if mibBuilder.loadTexts: basCpeAddressEntry.setDescription('')
basCpeAddressIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCpeAddressIdx.setStatus('current')
if mibBuilder.loadTexts: basCpeAddressIdx.setDescription('')
basCpeAddressMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCpeAddressMacAddr.setStatus('current')
if mibBuilder.loadTexts: basCpeAddressMacAddr.setDescription('')
basCmBpiSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17))
basCmBpiAuthWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiAuthWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: basCmBpiAuthWaitTimeout.setDescription('')
basCmBpiReAuthWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiReAuthWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: basCmBpiReAuthWaitTimeout.setDescription('')
basCmBpiAuthGraceTime = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiAuthGraceTime.setStatus('current')
if mibBuilder.loadTexts: basCmBpiAuthGraceTime.setDescription('')
basCmBpiOperWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiOperWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: basCmBpiOperWaitTimeout.setDescription('')
basCmBpiRekeyWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiRekeyWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: basCmBpiRekeyWaitTimeout.setDescription('')
basCmBpiTEKGraceTime = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiTEKGraceTime.setStatus('current')
if mibBuilder.loadTexts: basCmBpiTEKGraceTime.setDescription('')
basCmBpiAuthRejectWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiAuthRejectWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: basCmBpiAuthRejectWaitTimeout.setDescription('')
basCmBpiSAMapWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiSAMapWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: basCmBpiSAMapWaitTimeout.setDescription('')
basCmBpiMaxClockDrift = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiMaxClockDrift.setStatus('current')
if mibBuilder.loadTexts: basCmBpiMaxClockDrift.setDescription('')
basCmBpiSAMapMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmBpiSAMapMaxRetries.setStatus('current')
if mibBuilder.loadTexts: basCmBpiSAMapMaxRetries.setDescription('')
basCmMaxNumCPEs = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmMaxNumCPEs.setStatus('current')
if mibBuilder.loadTexts: basCmMaxNumCPEs.setDescription('The maximum number of CPEs that can be granted access through a CM during a CM epoch. The maximum number of CPEs MUST be enforced by the CM.')
basCmMIC = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 256), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmMIC.setStatus('current')
if mibBuilder.loadTexts: basCmMIC.setDescription('')
basCmtsMIC = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 257), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basCmtsMIC.setStatus('current')
if mibBuilder.loadTexts: basCmtsMIC.setDescription('')
basCmEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 258), Integer32())
if mibBuilder.loadTexts: basCmEndOfMib.setStatus('current')
if mibBuilder.loadTexts: basCmEndOfMib.setDescription('This object is used to mark the end of the cable modem configuration MIB. Add any new objects before this object. Do not add any cable modem configuration objects after this object.')
mibBuilder.exportSymbols("BAS-CM-CONFIG-MIB", basSnmpMibObjectTable=basSnmpMibObjectTable, basCmBpiSettings=basCmBpiSettings, basCpeAddressIdx=basCpeAddressIdx, basCmBpiOperWaitTimeout=basCmBpiOperWaitTimeout, basSnmpMibObjectIdx=basSnmpMibObjectIdx, basCmBpiAuthGraceTime=basCmBpiAuthGraceTime, basCmCosGuaranteedUsBps=basCmCosGuaranteedUsBps, basCmCosTable=basCmCosTable, basCmCosUsPriority=basCmCosUsPriority, basCmCosMaxUsBps=basCmCosMaxUsBps, basCmNetworkAccess=basCmNetworkAccess, basCmUsChannelId=basCmUsChannelId, basCmBpiMaxClockDrift=basCmBpiMaxClockDrift, basCmMIC=basCmMIC, basCmBpiTEKGraceTime=basCmBpiTEKGraceTime, basCmBpiAuthRejectWaitTimeout=basCmBpiAuthRejectWaitTimeout, basCmBpiAuthWaitTimeout=basCmBpiAuthWaitTimeout, basCmtsMIC=basCmtsMIC, basCmCosBp=basCmCosBp, basCpeAddressMacAddr=basCpeAddressMacAddr, PYSNMP_MODULE_ID=basCmConfigMIB, basCpeAddressEntry=basCpeAddressEntry, basCmEndOfMib=basCmEndOfMib, basCpeAddressTable=basCpeAddressTable, basCmCapabilities=basCmCapabilities, basCmBpiSAMapMaxRetries=basCmBpiSAMapMaxRetries, basCmCapConcat=basCmCapConcat, basCmCosMaxUsBurst=basCmCosMaxUsBurst, basCmBpiReAuthWaitTimeout=basCmBpiReAuthWaitTimeout, basCmBpiRekeyWaitTimeout=basCmBpiRekeyWaitTimeout, basCmConfigMIB=basCmConfigMIB, basCmMaxNumCPEs=basCmMaxNumCPEs, basCmCosClassId=basCmCosClassId, basCmCosMaxDsBps=basCmCosMaxDsBps, basSnmpMibObjectEntry=basSnmpMibObjectEntry, basCmCosEntry=basCmCosEntry, basSnmpMibObjectVarBind=basSnmpMibObjectVarBind, basCmDsFreq=basCmDsFreq, basCmBpiSAMapWaitTimeout=basCmBpiSAMapWaitTimeout)
