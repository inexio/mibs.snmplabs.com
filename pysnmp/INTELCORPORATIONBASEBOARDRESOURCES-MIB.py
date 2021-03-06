#
# PySNMP MIB module INTELCORPORATIONBASEBOARDRESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATIONBASEBOARDRESOURCES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Counter64, ModuleIdentity, Unsigned32, Counter32, enterprises, MibIdentifier, ObjectIdentity, Integer32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Counter64", "ModuleIdentity", "Unsigned32", "Counter32", "enterprises", "MibIdentifier", "ObjectIdentity", "Integer32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DmiInteger(Integer32):
    pass

class DmiInteger64X(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-18446744073709551615, 18446744073709551615)

class DmiDisplaystring(DisplayString):
    pass

class DmiDateX(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(28, 28)
    fixedLength = 28

class DmiComponentIndex(Integer32):
    pass

intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2))
server_products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 6)).setLabel("server-products")
platforms = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 6, 2))
resources = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3))
dmtfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1))
tComponentid = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1), )
if mibBuilder.loadTexts: tComponentid.setStatus('mandatory')
eComponentid = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eComponentid.setStatus('mandatory')
a1Manufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Manufacturer.setStatus('mandatory')
a1Product = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Product.setStatus('mandatory')
a1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Version.setStatus('mandatory')
a1SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1SerialNumber.setStatus('mandatory')
a1Installation = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 5), DmiDateX()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Installation.setStatus('mandatory')
a1Verify = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vAnErrorOccurredCheckStatusCode", 0), ("vThisComponentDoesNotExist", 1), ("vVerificationIsNotSupported", 2), ("vReserved", 3), ("vThisComponentExistsButTheFunctionalityI", 4), ("vThisComponentExistsButTheFunctionality1", 5), ("vThisComponentExistsAndIsNotFunctioningC", 6), ("vThisComponentExistsAndIsFunctioningCorr", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Verify.setStatus('mandatory')
tSystemResources2 = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41), )
if mibBuilder.loadTexts: tSystemResources2.setStatus('mandatory')
eSystemResources2 = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a41SystemResourcesIndex"))
if mibBuilder.loadTexts: eSystemResources2.setStatus('mandatory')
a41SystemResourcesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41SystemResourcesIndex.setStatus('mandatory')
a41ResourceUser = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceUser.setStatus('mandatory')
a41ResourceSet = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceSet.setStatus('mandatory')
a41ResourceAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vAllocated", 3), ("vAssignable", 4), ("vTemporaryAssignment", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceAssignment.setStatus('mandatory')
a41ResourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vMemory", 3), ("vIo", 4), ("vIrq", 5), ("vDma", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceType.setStatus('mandatory')
a41ResourceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceNumber.setStatus('mandatory')
a41ResourceInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceInfoId.setStatus('mandatory')
a41StartAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 8), DmiInteger64X()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41StartAddress.setStatus('mandatory')
a41EndAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 9), DmiInteger64X()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41EndAddress.setStatus('mandatory')
a41ResourceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 10), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41ResourceSize.setStatus('mandatory')
a41BaseAlignment = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 11), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41BaseAlignment.setStatus('mandatory')
a41Shareable = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1), ("vUnknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41Shareable.setStatus('mandatory')
a41Shared = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1), ("vUnknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a41Shared.setStatus('mandatory')
tSystemResourceDeviceInfo = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42), )
if mibBuilder.loadTexts: tSystemResourceDeviceInfo.setStatus('mandatory')
eSystemResourceDeviceInfo = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a42ResourceUser"))
if mibBuilder.loadTexts: eSystemResourceDeviceInfo.setStatus('mandatory')
a42ResourceUser = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42ResourceUser.setStatus('mandatory')
a42DeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42DeviceId.setStatus('mandatory')
a42DeviceSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42DeviceSerialNumber.setStatus('mandatory')
a42LogicalDeviceId_ClassCode = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 4), DmiInteger()).setLabel("a42LogicalDeviceId-ClassCode").setMaxAccess("readonly")
if mibBuilder.loadTexts: a42LogicalDeviceId_ClassCode.setStatus('mandatory')
a42DeviceFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42DeviceFlags.setStatus('mandatory')
a42DeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42DeviceNumber.setStatus('mandatory')
a42FunctionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42FunctionNumber.setStatus('mandatory')
a42BusType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 8), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42BusType.setStatus('mandatory')
a42CmReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 9), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a42CmReserved.setStatus('mandatory')
tSystemResourceMemoryInfo = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43), )
if mibBuilder.loadTexts: tSystemResourceMemoryInfo.setStatus('mandatory')
eSystemResourceMemoryInfo = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a43SystemResourceMemoryInfoIndex"))
if mibBuilder.loadTexts: eSystemResourceMemoryInfo.setStatus('mandatory')
a43SystemResourceMemoryInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a43SystemResourceMemoryInfoIndex.setStatus('mandatory')
a43IsapcmciaRangeDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("v8-bitMemoryOnly", 3), ("v16-bitMemoryOnly", 4), ("v8-And16-bitMemorySupported", 5), ("v32-bitMemoryOnly", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a43IsapcmciaRangeDescriptor.setStatus('mandatory')
a43EisaRangeDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("v8-bitMemoryOnly", 3), ("v16-bitMemoryOnly", 4), ("v8-And16-bitMemorySupported", 5), ("v32-bitMemoryOnly", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a43EisaRangeDescriptor.setStatus('mandatory')
a43DecodeSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vDecodeSupportsHighAddress", 3), ("vDecodeSupportsRangeLength", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a43DecodeSupport.setStatus('mandatory')
a43Cacheable = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1), ("vUnknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a43Cacheable.setStatus('mandatory')
a43CacheType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vWrite-back", 3), ("vWrite-through", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a43CacheType.setStatus('mandatory')
a43Read_write = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vRomReadOnly", 3), ("vRamReadwrite", 4)))).setLabel("a43Read-write").setMaxAccess("readonly")
if mibBuilder.loadTexts: a43Read_write.setStatus('mandatory')
tSystemResourceIoInfo = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44), )
if mibBuilder.loadTexts: tSystemResourceIoInfo.setStatus('mandatory')
eSystemResourceIoInfo = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a44SystemResourceIoInfoIndex"))
if mibBuilder.loadTexts: eSystemResourceIoInfo.setStatus('mandatory')
a44SystemResourceIoInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a44SystemResourceIoInfoIndex.setStatus('mandatory')
a44IoDecode = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("v10Bits", 3), ("v16Bits", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a44IoDecode.setStatus('mandatory')
tSystemResourceIrqInfo = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45), )
if mibBuilder.loadTexts: tSystemResourceIrqInfo.setStatus('mandatory')
eSystemResourceIrqInfo = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a45SystemResourceIrqInfoIndex"))
if mibBuilder.loadTexts: eSystemResourceIrqInfo.setStatus('mandatory')
a45SystemResourceIrqInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a45SystemResourceIrqInfoIndex.setStatus('mandatory')
a45TriggerType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vLevel", 3), ("vEdge", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a45TriggerType.setStatus('mandatory')
a45TriggerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vActiveLow", 3), ("vActiveHigh", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a45TriggerLevel.setStatus('mandatory')
tSystemResourceDmaInfo = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46), )
if mibBuilder.loadTexts: tSystemResourceDmaInfo.setStatus('mandatory')
eSystemResourceDmaInfo = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"), (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a46SystemResourceDmaInfoIndex"))
if mibBuilder.loadTexts: eSystemResourceDmaInfo.setStatus('mandatory')
a46SystemResourceDmaInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46SystemResourceDmaInfoIndex.setStatus('mandatory')
a46DmaTransferWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("v8-bit", 3), ("v8-And16-bit", 4), ("v16-bit", 5), ("v32-bit", 6), ("v64-bit", 7), ("v128-bit", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46DmaTransferWidth.setStatus('mandatory')
a46DmaAddressSize = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("v8-bit", 3), ("v16-bit", 5), ("v32-bit", 6), ("v64-bit", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46DmaAddressSize.setStatus('mandatory')
a46DmaMaximumTransferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46DmaMaximumTransferSize.setStatus('mandatory')
a46DmaTransferPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("v8-bit", 3), ("v8-And16-bit", 4), ("v16-bit", 5), ("v32-bit", 6), ("v64-bit", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46DmaTransferPreference.setStatus('mandatory')
a46BusMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vLogicalDeviceIsNotABusMaster", 3), ("vLogicalDeviceIsABusMaster", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46BusMaster.setStatus('mandatory')
a46ByteMode = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vDmaMayNotExecuteInCountByByteMode", 3), ("vDmaMayExecuteInCountByByteMode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46ByteMode.setStatus('mandatory')
a46WordMode = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vDmaMayNotExecuteInCountByWordMode", 3), ("vDmaMayExecuteInCountByWordMode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46WordMode.setStatus('mandatory')
a46ChannelTiming = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vIsaCompatible", 3), ("vTypeA", 4), ("vTypeB", 5), ("vTypeF", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a46ChannelTiming.setStatus('mandatory')
a46Type_cTiming = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2), ("vIsaCompatible", 3), ("vCTypeTimingIsNotSupported", 4), ("vCTypeTimingIsSupported", 5)))).setLabel("a46Type-cTiming").setMaxAccess("readonly")
if mibBuilder.loadTexts: a46Type_cTiming.setStatus('mandatory')
tMiftomib = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001), )
if mibBuilder.loadTexts: tMiftomib.setStatus('mandatory')
eMiftomib = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1), ).setIndexNames((0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eMiftomib.setStatus('mandatory')
a1001MibName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1001MibName.setStatus('mandatory')
a1001MibOid = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1001MibOid.setStatus('mandatory')
a1001DisableTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1, 3), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a1001DisableTrap.setStatus('mandatory')
mibBuilder.exportSymbols("INTELCORPORATIONBASEBOARDRESOURCES-MIB", a42BusType=a42BusType, a1Product=a1Product, a41StartAddress=a41StartAddress, a41ResourceUser=a41ResourceUser, a42DeviceId=a42DeviceId, a43CacheType=a43CacheType, tSystemResourceIrqInfo=tSystemResourceIrqInfo, a41ResourceType=a41ResourceType, a42FunctionNumber=a42FunctionNumber, tComponentid=tComponentid, DmiDateX=DmiDateX, a46DmaMaximumTransferSize=a46DmaMaximumTransferSize, tMiftomib=tMiftomib, tSystemResourceDmaInfo=tSystemResourceDmaInfo, a46WordMode=a46WordMode, a1001MibName=a1001MibName, platforms=platforms, eSystemResourceDmaInfo=eSystemResourceDmaInfo, eComponentid=eComponentid, a43EisaRangeDescriptor=a43EisaRangeDescriptor, tSystemResources2=tSystemResources2, dmtfGroups=dmtfGroups, a43SystemResourceMemoryInfoIndex=a43SystemResourceMemoryInfoIndex, a1Verify=a1Verify, resources=resources, a41ResourceSize=a41ResourceSize, eSystemResources2=eSystemResources2, eSystemResourceDeviceInfo=eSystemResourceDeviceInfo, a46ByteMode=a46ByteMode, a45SystemResourceIrqInfoIndex=a45SystemResourceIrqInfoIndex, a44IoDecode=a44IoDecode, eSystemResourceMemoryInfo=eSystemResourceMemoryInfo, tSystemResourceDeviceInfo=tSystemResourceDeviceInfo, a41Shared=a41Shared, a46Type_cTiming=a46Type_cTiming, a41ResourceInfoId=a41ResourceInfoId, a1Installation=a1Installation, a43IsapcmciaRangeDescriptor=a43IsapcmciaRangeDescriptor, intel=intel, a1Version=a1Version, a41EndAddress=a41EndAddress, DmiInteger64X=DmiInteger64X, DmiInteger=DmiInteger, a41SystemResourcesIndex=a41SystemResourcesIndex, a41BaseAlignment=a41BaseAlignment, a42DeviceFlags=a42DeviceFlags, a43DecodeSupport=a43DecodeSupport, a42DeviceNumber=a42DeviceNumber, a45TriggerType=a45TriggerType, products=products, a45TriggerLevel=a45TriggerLevel, a1Manufacturer=a1Manufacturer, server_products=server_products, a41ResourceAssignment=a41ResourceAssignment, a1SerialNumber=a1SerialNumber, a41ResourceSet=a41ResourceSet, a46DmaTransferPreference=a46DmaTransferPreference, a46SystemResourceDmaInfoIndex=a46SystemResourceDmaInfoIndex, DmiComponentIndex=DmiComponentIndex, a46BusMaster=a46BusMaster, a43Read_write=a43Read_write, a43Cacheable=a43Cacheable, a42ResourceUser=a42ResourceUser, a46DmaAddressSize=a46DmaAddressSize, a46DmaTransferWidth=a46DmaTransferWidth, eMiftomib=eMiftomib, tSystemResourceMemoryInfo=tSystemResourceMemoryInfo, a42LogicalDeviceId_ClassCode=a42LogicalDeviceId_ClassCode, a1001MibOid=a1001MibOid, a41Shareable=a41Shareable, DmiDisplaystring=DmiDisplaystring, tSystemResourceIoInfo=tSystemResourceIoInfo, a41ResourceNumber=a41ResourceNumber, eSystemResourceIrqInfo=eSystemResourceIrqInfo, a42CmReserved=a42CmReserved, a1001DisableTrap=a1001DisableTrap, a46ChannelTiming=a46ChannelTiming, a44SystemResourceIoInfoIndex=a44SystemResourceIoInfoIndex, a42DeviceSerialNumber=a42DeviceSerialNumber, eSystemResourceIoInfo=eSystemResourceIoInfo)
