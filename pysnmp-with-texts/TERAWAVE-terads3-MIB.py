#
# PySNMP MIB module TERAWAVE-terads3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-terads3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, TimeTicks, Unsigned32, NotificationType, ObjectIdentity, iso, Gauge32, ModuleIdentity, IpAddress, Bits, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "Unsigned32", "NotificationType", "ObjectIdentity", "iso", "Gauge32", "ModuleIdentity", "IpAddress", "Bits", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
teraCDS3Group = MibIdentifier((1, 3, 6, 1, 4, 1, 4513, 8))
teraDSX3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 1), )
if mibBuilder.loadTexts: teraDSX3ConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3ConfigTable.setDescription(' table teraDSX3ConfigTable')
teraDSX3ConfigTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "teraDs3LineIndex"))
if mibBuilder.loadTexts: teraDSX3ConfigTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3ConfigTableEntry.setDescription(' table entry teraDSX3ConfigTableEntry ')
teraDs3LineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDs3LineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3LineIndex.setDescription('')
teraDs3OOFCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bits3Of8", 1), ("bits3Of16", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraDs3OOFCriteria.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3OOFCriteria.setDescription('')
teraDs3AISBitsChkSchm = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("checkCbits", 1), ("ignoreBits", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraDs3AISBitsChkSchm.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3AISBitsChkSchm.setDescription('')
teraDs3RcvFEACCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fEACCodes4Of5", 1), ("fEACCodes8Of16", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraDs3RcvFEACCriteria.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3RcvFEACCriteria.setDescription('')
teraDs3FEACLoopCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraDs3FEACLoopCheck.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3FEACLoopCheck.setDescription('')
teraDs3DS1FarEndLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))).clone(namedValues=NamedValues(("none", 0), ("dS1-1", 1), ("dS1-2", 2), ("dS1-3", 3), ("dS1-4", 4), ("dS1-5", 5), ("dS1-6", 6), ("dS1-7", 7), ("dS1-8", 8), ("dS1-9", 9), ("dS1-10", 10), ("dS1-11", 11), ("dS1-12", 12), ("dS1-13", 13), ("dS1-14", 14), ("dS1-15", 15), ("dS1-16", 16), ("dS1-17", 17), ("dS1-18", 18), ("dS1-19", 19), ("dS1-20", 20), ("dS1-21", 21), ("dS1-22", 22), ("dS1-23", 23), ("dS1-24", 24), ("dS1-25", 25), ("dS1-26", 26), ("dS1-27", 27), ("dS1-28", 28), ("all-DS1", 29)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDs3DS1FarEndLoopStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3DS1FarEndLoopStatus.setDescription('')
teraDs3DS1NearEndLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))).clone(namedValues=NamedValues(("none", 0), ("dS1-1", 1), ("dS1-2", 2), ("dS1-3", 3), ("dS1-4", 4), ("dS1-5", 5), ("dS1-6", 6), ("dS1-7", 7), ("dS1-8", 8), ("dS1-9", 9), ("dS1-10", 10), ("dS1-11", 11), ("dS1-12", 12), ("dS1-13", 13), ("dS1-14", 14), ("dS1-15", 15), ("dS1-16", 16), ("dS1-17", 17), ("dS1-18", 18), ("dS1-19", 19), ("dS1-20", 20), ("dS1-21", 21), ("dS1-22", 22), ("dS1-23", 23), ("dS1-24", 24), ("dS1-25", 25), ("dS1-26", 26), ("dS1-27", 27), ("dS1-28", 28), ("all-DS1", 29)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDs3DS1NearEndLoopStatus.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3DS1NearEndLoopStatus.setDescription('')
teraDs37DayTotalTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDs37DayTotalTimeElapsed.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs37DayTotalTimeElapsed.setDescription('')
teraDs3ExtendValidTotalIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDs3ExtendValidTotalIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3ExtendValidTotalIntervals.setDescription('')
teraDs3ExtendInvalidTotalIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDs3ExtendInvalidTotalIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: teraDs3ExtendInvalidTotalIntervals.setDescription('')
teraDSX37DayTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 2), )
if mibBuilder.loadTexts: teraDSX37DayTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX37DayTotalTable.setDescription(' table teraDSX37DayTotalTable')
teraDSX37DayTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "teraDS37DayTotalIndex"), (0, "TERAWAVE-terads3-MIB", "teraDS37DayTotalNumber"))
if mibBuilder.loadTexts: teraDSX37DayTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX37DayTotalTableEntry.setDescription(' table entry teraDSX37DayTotalTableEntry ')
teraDS37DayTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalIndex.setDescription('')
teraDS37DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalNumber.setDescription('')
teraDS37DayTotalPESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalPESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalPESs.setDescription('')
teraDS37DayTotalPSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalPSESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalPSESs.setDescription('')
teraDS37DayTotalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalSEFSs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalSEFSs.setDescription('')
teraDS37DayTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalUASs.setDescription('')
teraDS37DayTotalLCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalLCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalLCVs.setDescription('')
teraDS37DayTotalPCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalPCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalPCVs.setDescription('')
teraDS37DayTotalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalLESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalLESs.setDescription('')
teraDS37DayTotalCCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalCCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalCCVs.setDescription('')
teraDS37DayTotalCESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalCESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalCESs.setDescription('')
teraDS37DayTotalCSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalCSESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalCSESs.setDescription('')
teraDS37DayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS37DayTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS37DayTotalValidData.setDescription('')
teraDSX3FarEnd7DayTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 3), )
if mibBuilder.loadTexts: teraDSX3FarEnd7DayTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3FarEnd7DayTotalTable.setDescription(' table teraDSX3FarEnd7DayTotalTable')
teraDSX3FarEnd7DayTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "teraDSX3FarEnd7DayTotalIndex"), (0, "TERAWAVE-terads3-MIB", "teraDS3FarEnd7DayTotalNumber"))
if mibBuilder.loadTexts: teraDSX3FarEnd7DayTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3FarEnd7DayTotalTableEntry.setDescription(' table entry teraDSX3FarEnd7DayTotalTableEntry ')
teraDSX3FarEnd7DayTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDSX3FarEnd7DayTotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3FarEnd7DayTotalIndex.setDescription('')
teraDS3FarEnd7DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalNumber.setDescription('')
teraDS3FarEnd7DayTotalCESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalCESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalCESs.setDescription('')
teraDS3FarEnd7DayTotalCSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalCSESs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalCSESs.setDescription('')
teraDS3FarEnd7DayTotalCCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalCCVs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalCCVs.setDescription('')
teraDS3FarEnd7DayTotalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalUASs.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalUASs.setDescription('')
teraDS3FarEnd7DayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3FarEnd7DayTotalValidData.setDescription('')
teradsx3CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 4), )
if mibBuilder.loadTexts: teradsx3CurrentTable.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3CurrentTable.setDescription(' table teradsx3CurrentTable')
teradsx3CurrentTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "teradsx3CurrentIndex"))
if mibBuilder.loadTexts: teradsx3CurrentTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3CurrentTableEntry.setDescription(' table entry teradsx3CurrentTableEntry ')
teradsx3CurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3CurrentIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3CurrentIndex.setDescription('')
teradsx3ESB_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 2), Integer32()).setLabel("teradsx3ESB-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3ESB_L.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3ESB_L.setDescription('')
teradsx3LOSS_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 3), Gauge32()).setLabel("teradsx3LOSS-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3LOSS_L.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3LOSS_L.setDescription('')
teradsx3ESB_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 4), Gauge32()).setLabel("teradsx3ESB-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3ESB_P.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3ESB_P.setDescription('')
teradsx3SAS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 5), Gauge32()).setLabel("teradsx3SAS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3SAS_P.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3SAS_P.setDescription('')
teradsx3AISS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 6), Gauge32()).setLabel("teradsx3AISS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3AISS_P.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3AISS_P.setDescription('')
teradsx3UASP_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 7), Gauge32()).setLabel("teradsx3UASP-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3UASP_P.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3UASP_P.setDescription('')
teradsx3ESCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 8), Gauge32()).setLabel("teradsx3ESCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3ESCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3ESCP_PFE.setDescription('')
teradsx3ESBCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 9), Gauge32()).setLabel("teradsx3ESBCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3ESBCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3ESBCP_PFE.setDescription('')
teradsx3SASCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 10), Gauge32()).setLabel("teradsx3SASCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: teradsx3SASCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3SASCP_PFE.setDescription('')
teradsx3IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 5), )
if mibBuilder.loadTexts: teradsx3IntervalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3IntervalTable.setDescription(' table teradsx3IntervalTable')
teradsx3IntervalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "terads3IntervalIndex"), (0, "TERAWAVE-terads3-MIB", "terads3IntervalNumber"))
if mibBuilder.loadTexts: teradsx3IntervalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3IntervalTableEntry.setDescription(' table entry teradsx3IntervalTableEntry ')
terads3IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3IntervalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: terads3IntervalIndex.setDescription('')
terads3IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3IntervalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: terads3IntervalNumber.setDescription('')
terads3Intervalteradsx3ESB_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 3), Gauge32()).setLabel("terads3Intervalteradsx3ESB-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3ESB_L.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3ESB_L.setDescription('')
terads3Intervalteradsx3LOSS_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 4), Gauge32()).setLabel("terads3Intervalteradsx3LOSS-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3LOSS_L.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3LOSS_L.setDescription('')
terads3Intervalteradsx3ESB_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 5), Gauge32()).setLabel("terads3Intervalteradsx3ESB-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3ESB_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3ESB_P.setDescription('')
terads3Intervalteradsx3SAS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 6), Gauge32()).setLabel("terads3Intervalteradsx3SAS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3SAS_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3SAS_P.setDescription('')
terads3Intervalteradsx3AISS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 7), Gauge32()).setLabel("terads3Intervalteradsx3AISS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3AISS_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3AISS_P.setDescription('')
terads3Intervalteradsx3UASP_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 8), Gauge32()).setLabel("terads3Intervalteradsx3UASP-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3UASP_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3UASP_P.setDescription('')
terads3Intervalteradsx3ESCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 9), Gauge32()).setLabel("terads3Intervalteradsx3ESCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3ESCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3ESCP_PFE.setDescription('')
terads3Intervalteradsx3ESBCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 10), Gauge32()).setLabel("terads3Intervalteradsx3ESBCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3ESBCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3ESBCP_PFE.setDescription('')
terads3Intervalteradsx3SASCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 11), Gauge32()).setLabel("terads3Intervalteradsx3SASCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Intervalteradsx3SASCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Intervalteradsx3SASCP_PFE.setDescription('')
terads3IntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3IntervalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: terads3IntervalValidData.setDescription('')
teradsx3TotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 6), )
if mibBuilder.loadTexts: teradsx3TotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3TotalTable.setDescription(' table teradsx3TotalTable')
teradsx3TotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "terads3TotalIndex"))
if mibBuilder.loadTexts: teradsx3TotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teradsx3TotalTableEntry.setDescription(' table entry teradsx3TotalTableEntry ')
terads3TotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3TotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: terads3TotalIndex.setDescription('')
terads3Totalteradsx3ESB_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 2), Gauge32()).setLabel("terads3Totalteradsx3ESB-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3ESB_L.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3ESB_L.setDescription('')
terads3Totalteradsx3LOSS_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 3), Gauge32()).setLabel("terads3Totalteradsx3LOSS-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3LOSS_L.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3LOSS_L.setDescription('')
terads3Totalteradsx3ESB_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 4), Gauge32()).setLabel("terads3Totalteradsx3ESB-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3ESB_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3ESB_P.setDescription('')
terads3Totalteradsx3SAS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 5), Gauge32()).setLabel("terads3Totalteradsx3SAS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3SAS_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3SAS_P.setDescription('')
terads3Totalteradsx3AISS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 6), Gauge32()).setLabel("terads3Totalteradsx3AISS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3AISS_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3AISS_P.setDescription('')
terads3Totalteradsx3UASP_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 7), Gauge32()).setLabel("terads3Totalteradsx3UASP-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3UASP_P.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3UASP_P.setDescription('')
terads3Totalteradsx3ESCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 8), Gauge32()).setLabel("terads3Totalteradsx3ESCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3ESCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3ESCP_PFE.setDescription('')
terads3Totalteradsx3ESBCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 9), Gauge32()).setLabel("terads3Totalteradsx3ESBCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3ESBCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3ESBCP_PFE.setDescription('')
terads3Totalteradsx3SASCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 10), Gauge32()).setLabel("terads3Totalteradsx3SASCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: terads3Totalteradsx3SASCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: terads3Totalteradsx3SASCP_PFE.setDescription('')
terads3TotalPerfStat = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: terads3TotalPerfStat.setStatus('mandatory')
if mibBuilder.loadTexts: terads3TotalPerfStat.setDescription('')
teraDSX3tera7DayTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 8, 7), )
if mibBuilder.loadTexts: teraDSX3tera7DayTotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3tera7DayTotalTable.setDescription(' table teraDSX3tera7DayTotalTable')
teraDSX3tera7DayTotalTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1), ).setIndexNames((0, "TERAWAVE-terads3-MIB", "teraDSX3tera7DayTotalIndex"), (0, "TERAWAVE-terads3-MIB", "teraDS3tera7DayTotalNumber"))
if mibBuilder.loadTexts: teraDSX3tera7DayTotalTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3tera7DayTotalTableEntry.setDescription(' table entry teraDSX3tera7DayTotalTableEntry ')
teraDSX3tera7DayTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDSX3tera7DayTotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teraDSX3tera7DayTotalIndex.setDescription('')
teraDS3tera7DayTotalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalNumber.setDescription('')
teraDS3tera7DayTotalteradsx3ESB_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 3), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3ESB-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESB_L.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESB_L.setDescription('')
teraDS3tera7DayTotalteradsx3LOSS_L = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 4), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3LOSS-L").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3LOSS_L.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3LOSS_L.setDescription('')
teraDS3tera7DayTotalteradsx3ESB_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 5), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3ESB-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESB_P.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESB_P.setDescription('')
teraDS3tera7DayTotalteradsx3SAS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 6), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3SAS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3SAS_P.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3SAS_P.setDescription('')
teraDS3tera7DayTotalteradsx3AISS_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 7), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3AISS-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3AISS_P.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3AISS_P.setDescription('')
teraDS3tera7DayTotalteradsx3UASP_P = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 8), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3UASP-P").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3UASP_P.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3UASP_P.setDescription('')
teraDS3tera7DayTotalteradsx3ESCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 9), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3ESCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESCP_PFE.setDescription('')
teraDS3tera7DayTotalteradsx3ESBCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 10), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3ESBCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESBCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3ESBCP_PFE.setDescription('')
teraDS3tera7DayTotalteradsx3SASCP_PFE = MibScalar((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 11), Gauge32()).setLabel("teraDS3tera7DayTotalteradsx3SASCP-PFE").setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3SASCP_PFE.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalteradsx3SASCP_PFE.setDescription('')
teraDS3tera7DayTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraDS3tera7DayTotalValidData.setStatus('mandatory')
if mibBuilder.loadTexts: teraDS3tera7DayTotalValidData.setDescription('')
mibBuilder.exportSymbols("TERAWAVE-terads3-MIB", teraDS3tera7DayTotalteradsx3LOSS_L=teraDS3tera7DayTotalteradsx3LOSS_L, terads3Totalteradsx3SASCP_PFE=terads3Totalteradsx3SASCP_PFE, terads3Totalteradsx3ESBCP_PFE=terads3Totalteradsx3ESBCP_PFE, terads3Intervalteradsx3ESB_P=terads3Intervalteradsx3ESB_P, terads3Totalteradsx3AISS_P=terads3Totalteradsx3AISS_P, teraDs3ExtendInvalidTotalIntervals=teraDs3ExtendInvalidTotalIntervals, terads3Intervalteradsx3ESBCP_PFE=terads3Intervalteradsx3ESBCP_PFE, teradsx3ESB_P=teradsx3ESB_P, terads3Totalteradsx3ESB_P=terads3Totalteradsx3ESB_P, teraDS37DayTotalIndex=teraDS37DayTotalIndex, teradsx3SAS_P=teradsx3SAS_P, teraDS37DayTotalLCVs=teraDS37DayTotalLCVs, terads3Totalteradsx3ESCP_PFE=terads3Totalteradsx3ESCP_PFE, teraDSX3ConfigTable=teraDSX3ConfigTable, teraDs3AISBitsChkSchm=teraDs3AISBitsChkSchm, teradsx3TotalTable=teradsx3TotalTable, teraDS37DayTotalPESs=teraDS37DayTotalPESs, teraDS37DayTotalNumber=teraDS37DayTotalNumber, teradsx3SASCP_PFE=teradsx3SASCP_PFE, terads3TotalIndex=terads3TotalIndex, terads3TotalPerfStat=terads3TotalPerfStat, teraDSX3tera7DayTotalTable=teraDSX3tera7DayTotalTable, terads3Intervalteradsx3AISS_P=terads3Intervalteradsx3AISS_P, teradsx3ESB_L=teradsx3ESB_L, terads3Intervalteradsx3ESCP_PFE=terads3Intervalteradsx3ESCP_PFE, teradsx3LOSS_L=teradsx3LOSS_L, teradsx3UASP_P=teradsx3UASP_P, terawave=terawave, teraDS3tera7DayTotalteradsx3ESB_P=teraDS3tera7DayTotalteradsx3ESB_P, teraDS3tera7DayTotalteradsx3ESB_L=teraDS3tera7DayTotalteradsx3ESB_L, teraDS3FarEnd7DayTotalValidData=teraDS3FarEnd7DayTotalValidData, teraDS3FarEnd7DayTotalUASs=teraDS3FarEnd7DayTotalUASs, teradsx3CurrentTableEntry=teradsx3CurrentTableEntry, terads3Totalteradsx3ESB_L=terads3Totalteradsx3ESB_L, teradsx3TotalTableEntry=teradsx3TotalTableEntry, terads3Intervalteradsx3SAS_P=terads3Intervalteradsx3SAS_P, teraDS3tera7DayTotalteradsx3AISS_P=teraDS3tera7DayTotalteradsx3AISS_P, teraDS3tera7DayTotalteradsx3SAS_P=teraDS3tera7DayTotalteradsx3SAS_P, teraDS3tera7DayTotalteradsx3UASP_P=teraDS3tera7DayTotalteradsx3UASP_P, teraDS37DayTotalLESs=teraDS37DayTotalLESs, teraDS37DayTotalCCVs=teraDS37DayTotalCCVs, teraDS37DayTotalSEFSs=teraDS37DayTotalSEFSs, teradsx3AISS_P=teradsx3AISS_P, terads3Intervalteradsx3LOSS_L=terads3Intervalteradsx3LOSS_L, teradsx3ESCP_PFE=teradsx3ESCP_PFE, teraDS37DayTotalValidData=teraDS37DayTotalValidData, teraDSX3tera7DayTotalIndex=teraDSX3tera7DayTotalIndex, teraDS37DayTotalCSESs=teraDS37DayTotalCSESs, terads3Intervalteradsx3UASP_P=terads3Intervalteradsx3UASP_P, terads3Totalteradsx3UASP_P=terads3Totalteradsx3UASP_P, teraDS3tera7DayTotalteradsx3SASCP_PFE=teraDS3tera7DayTotalteradsx3SASCP_PFE, teraDs3RcvFEACCriteria=teraDs3RcvFEACCriteria, terads3Totalteradsx3LOSS_L=terads3Totalteradsx3LOSS_L, teraDS37DayTotalPSESs=teraDS37DayTotalPSESs, teraDs3ExtendValidTotalIntervals=teraDs3ExtendValidTotalIntervals, teraDS3tera7DayTotalValidData=teraDS3tera7DayTotalValidData, teradsx3IntervalTableEntry=teradsx3IntervalTableEntry, teradsx3CurrentIndex=teradsx3CurrentIndex, teraDS3tera7DayTotalteradsx3ESBCP_PFE=teraDS3tera7DayTotalteradsx3ESBCP_PFE, teraDSX3FarEnd7DayTotalTable=teraDSX3FarEnd7DayTotalTable, teraDS3FarEnd7DayTotalNumber=teraDS3FarEnd7DayTotalNumber, teradsx3ESBCP_PFE=teradsx3ESBCP_PFE, teraDSX3tera7DayTotalTableEntry=teraDSX3tera7DayTotalTableEntry, teraDSX37DayTotalTableEntry=teraDSX37DayTotalTableEntry, teradsx3IntervalTable=teradsx3IntervalTable, terads3IntervalNumber=terads3IntervalNumber, teraDs3DS1NearEndLoopStatus=teraDs3DS1NearEndLoopStatus, terads3IntervalIndex=terads3IntervalIndex, teraDS3tera7DayTotalNumber=teraDS3tera7DayTotalNumber, teraDS37DayTotalCESs=teraDS37DayTotalCESs, teraDSX37DayTotalTable=teraDSX37DayTotalTable, teraDs37DayTotalTimeElapsed=teraDs37DayTotalTimeElapsed, terads3Totalteradsx3SAS_P=terads3Totalteradsx3SAS_P, teraCDS3Group=teraCDS3Group, teraDs3OOFCriteria=teraDs3OOFCriteria, teraDS3FarEnd7DayTotalCSESs=teraDS3FarEnd7DayTotalCSESs, teraDs3LineIndex=teraDs3LineIndex, teradsx3CurrentTable=teradsx3CurrentTable, terads3IntervalValidData=terads3IntervalValidData, teraDs3FEACLoopCheck=teraDs3FEACLoopCheck, teraDs3DS1FarEndLoopStatus=teraDs3DS1FarEndLoopStatus, teraDS3FarEnd7DayTotalCCVs=teraDS3FarEnd7DayTotalCCVs, terads3Intervalteradsx3SASCP_PFE=terads3Intervalteradsx3SASCP_PFE, teraDS3FarEnd7DayTotalCESs=teraDS3FarEnd7DayTotalCESs, teraDSX3FarEnd7DayTotalTableEntry=teraDSX3FarEnd7DayTotalTableEntry, teraDS37DayTotalUASs=teraDS37DayTotalUASs, terads3Intervalteradsx3ESB_L=terads3Intervalteradsx3ESB_L, teraDS3tera7DayTotalteradsx3ESCP_PFE=teraDS3tera7DayTotalteradsx3ESCP_PFE, teraDSX3ConfigTableEntry=teraDSX3ConfigTableEntry, teraDS37DayTotalPCVs=teraDS37DayTotalPCVs, teraDSX3FarEnd7DayTotalIndex=teraDSX3FarEnd7DayTotalIndex)
