<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    extension-element-prefixes="">

    <xsl:output method="text" version="1.0" indent="no" omit-xml-declaration="yes"/>

    <xsl:template match="/">
        <xsl:apply-templates select="menu/category/resource/url"/>
    </xsl:template>

    <xsl:template match='url'>
        <xsl:choose>
            <xsl:when test="starts-with(., 'ftp:')"></xsl:when>
            <xsl:when test="starts-with(., '/')">
                <xsl:value-of select="concat('http://www.ncbi.nlm.nih.gov', .)"/>
<xsl:text> 
</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="."/>
<xsl:text>
</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
   </xsl:template>


</xsl:stylesheet>
