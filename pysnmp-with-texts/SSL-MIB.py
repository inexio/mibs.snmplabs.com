#
# PySNMP MIB module SSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SSL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, Counter64, Integer32, MibIdentifier, ModuleIdentity, Counter32, Unsigned32, ObjectIdentity, iso, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter64", "Integer32", "MibIdentifier", "ModuleIdentity", "Counter32", "Unsigned32", "ObjectIdentity", "iso", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swSSLMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 7))
if mibBuilder.loadTexts: swSSLMIB.setLastUpdated('9911220000Z')
if mibBuilder.loadTexts: swSSLMIB.setOrganization('Working Group')
if mibBuilder.loadTexts: swSSLMIB.setContactInfo(' ')
if mibBuilder.loadTexts: swSSLMIB.setDescription('The Secure Socket Layer MIB.')
swSSLMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 7, 1))
swSSLStatusAdmin = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLStatusAdmin.setStatus('current')
if mibBuilder.loadTexts: swSSLStatusAdmin.setDescription('This object indicates the SSL feature is support or not .')
swSSLCipherSuites = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 1, 2), Bits().clone(namedValues=NamedValues(("rsa-with-rc4-128-MD5", 0), ("rsa-with-3des-ede-cbc-sha", 1), ("dhe-dss-with-3des-ede-cbc-sha", 2), ("rsa-export-with-rc4-40-md5", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLCipherSuites.setStatus('current')
if mibBuilder.loadTexts: swSSLCipherSuites.setDescription('This object indicates the ciphersuites are enabled or not in the system. If the bit is 1 , indicate that ciphersuite is enabled , else is disabled . ')
swSSLCacheTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLCacheTimeout.setStatus('current')
if mibBuilder.loadTexts: swSSLCacheTimeout.setDescription('This object indicates the Cache Timeout value for SSL module to refresh the session resume data kept in database')
swSSLCertificateFile = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 7, 2))
swSSLCertificateFileIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLCertificateFileIPAddr.setStatus('current')
if mibBuilder.loadTexts: swSSLCertificateFileIPAddr.setDescription('The IP address where the file to be downloaded is located')
swSSLCertificateFilePath = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLCertificateFilePath.setStatus('current')
if mibBuilder.loadTexts: swSSLCertificateFilePath.setDescription('The description for the certificate file name included full path to be downloaded .')
swSSLCertificateKeyFilePath = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLCertificateKeyFilePath.setStatus('current')
if mibBuilder.loadTexts: swSSLCertificateKeyFilePath.setDescription('The description for the key file name included full path to be downloaded .')
swSSLCertificateFileCtrl = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("inactive", 2), ("start", 3), ("delete", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSSLCertificateFileCtrl.setStatus('current')
if mibBuilder.loadTexts: swSSLCertificateFileCtrl.setDescription('This object provides the user to download certificate or key file. ')
swSSLCertificateFileShowSatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("rsa", 2), ("dsa", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSSLCertificateFileShowSatus.setStatus('current')
if mibBuilder.loadTexts: swSSLCertificateFileShowSatus.setDescription('Show certificate file status.')
mibBuilder.exportSymbols("SSL-MIB", swSSLCertificateFilePath=swSSLCertificateFilePath, swSSLCertificateKeyFilePath=swSSLCertificateKeyFilePath, swSSLCacheTimeout=swSSLCacheTimeout, swSSLCertificateFileCtrl=swSSLCertificateFileCtrl, PYSNMP_MODULE_ID=swSSLMIB, swSSLCipherSuites=swSSLCipherSuites, swSSLCertificateFile=swSSLCertificateFile, swSSLMIB=swSSLMIB, swSSLStatusAdmin=swSSLStatusAdmin, swSSLCertificateFileIPAddr=swSSLCertificateFileIPAddr, swSSLMgmt=swSSLMgmt, swSSLCertificateFileShowSatus=swSSLCertificateFileShowSatus)
