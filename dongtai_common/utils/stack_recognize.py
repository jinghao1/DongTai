import marisa_trie

rules = [
    'aj.', 'akka.', 'android.', 'antlr.', 'apple.', 'aQute.', 'brave.', 'bsh.',
    'ch.qos.', 'co.paralleluniverse.', 'com.acumenat.', 'com.alibaba.arthas.',
    'com.alibaba.cloud.', 'com.alibaba.cola.', 'com.alibaba.com.caucho.',
    'com.alibaba.crr.', 'com.alibaba.csp.', 'com.alibaba.datax.',
    'com.alibaba.druid.', 'com.alibaba.dubbo.', 'com.alibaba.fastjson.',
    'com.alibaba.fastjson2.', 'com.alibaba.google.', 'com.alibaba.jvm.',
    'com.alibaba.metrics.', 'com.alibaba.nacos.', 'com.alibaba.otter.',
    'com.alibaba.rocketmq.', 'com.alibaba.rsqldb.', 'com.alibaba.spring.',
    'com.alibaba.ttl3.', 'com.alipay.common.', 'com.alipay.disruptor.',
    'com.alipay.hessian.', 'com.alipay.lookout.', 'com.alipay.remoting.',
    'com.alipay.sofa.', 'com.aliyun.openservices.', 'com.arjuna.',
    'com.asn1c.', 'com.atomikos.', 'com.baidu.bjf.', 'com.baidu.brpc.',
    'com.baidu.jprotobuf.', 'com.baomidou.', 'com.bea.', 'com.beust.',
    'com.carrotsearch.', 'com.caucho.', 'com.certicom.', 'com.codahale.',
    'com.corundumstudio.', 'com.ctc.', 'com.datastax.', 'com.ddtek.',
    'com.dyuproject.', 'com.esotericsoftware.', 'com.esri.', 'com.fasterxml.',
    'com.flipkart.', 'com.github.', 'com.google.', 'com.googlecode.',
    'com.headius.', 'com.ibm.', 'com.intellij.', 'com.jayway.', 'com.jcraft.',
    'com.kenai.', 'com.linar.', 'com.linecorp.', 'com.mchange.', 'com.merant.',
    'com.microsoft.', 'com.mkyong.', 'com.mongodb.', 'com.mysql.',
    'com.navercorp.', 'com.netflix.', 'com.networknt.', 'com.nimbusds.',
    'com.nulabinc.', 'com.octetstring.', 'com.octo.', 'com.opensymphony.',
    'com.oracle.', 'com.querydsl.', 'com.rabbitmq.', 'com.rsa.',
    'com.screener.', 'com.secnium.', 'com.solarmetric.', 'com.squareup.',
    'com.stoyanr.', 'com.sun.', 'com.tdunning.', 'com.terracotta.',
    'com.thetransactioncompany.', 'com.thoughtworks.', 'com.twitter.',
    'com.typesafe.', 'com.vividsolutions.', 'com.weibo.api.motan.', 'com.xxl.',
    'com.yahoo.', 'com.zaxxer.', 'com.zeroturnaround.', 'commonj.', 'dagger.',
    'de.javakaffee.', 'edu.emory.', 'feign.', 'freemarker.', 'gnu.', 'google.',
    'graphql.', 'groovy.', 'io.dongtai.', 'io.dropwizard.', 'io.github.',
    'io.grpc.', 'io.jsonwebtoken.', 'io.lettuce.', 'io.micrometer.',
    'io.netty.', 'io.opencensus.', 'io.opentelemetry.', 'io.opentracing.',
    'io.perfmark.', 'io.reactivex.', 'io.restassured.', 'io.shardingjdbc.',
    'io.shardingsphere.', 'io.swagger.', 'io.undertow.', 'io.vavr.',
    'io.vertx.', 'jain.', 'jakarta.', 'java.', 'javafx.', 'javassist.',
    'javax.', 'javelin.', 'jdk.', 'jersey.', 'jline.', 'jnr.', 'jodd.',
    'joptsimple.', 'jregex.', 'junit.', 'kodo.', 'lbmq.', 'mazz.', 'me.qmx.',
    'microsoft.', 'mozilla.', 'mssql.', 'net.bytebuddy.', 'net.iharder.',
    'net.jcip.', 'net.jpountz.', 'net.logstash.', 'net.minidev.', 'net.n3.',
    'net.rubyeye.', 'net.sf.', 'net.sourceforge.', 'net.spy.', 'netscape.',
    'nu.xom.', 'ognl.', 'okhttp3.', 'okio.', 'oracle.', 'org.abego.',
    'org.ajax4jsf.', 'org.antlr.', 'org.aopalliance.', 'org.apache.',
    'org.apiguardian.', 'org.asciidoctor.', 'org.aspectj.', 'org.assertj.',
    'org.attoparser.', 'org.bouncycastle.', 'org.bson.', 'org.ccil.',
    'org.checkerframework.', 'org.codehaus.', 'org.custommonkey.',
    'org.dataloader.', 'org.dom4j.', 'org.eclipse.', 'org.elasticsearch.',
    'org.flywaydb.', 'org.fusesource.', 'org.gjt.', 'org.glassfish.',
    'org.h2.', 'org.hamcrest.', 'org.hdiv.', 'org.HdrHistogram.',
    'org.hibernate.', 'org.hornetq.', 'org.hotswap.', 'org.hsqldb.',
    'org.I0Itec.', 'org.ietf.', 'org.jacoco.', 'org.jaxen.', 'org.jboss.',
    'org.jcodings.', 'org.jcp.', 'org.jctools.', 'org.jdom.', 'org.jetbrains.',
    'org.jfree.', 'org.jledit.', 'org.jnp.', 'org.joda.', 'org.joni.',
    'org.jose4j.', 'org.jruby.', 'org.json.', 'org.jsoup.', 'org.junit.',
    'org.jvnet.', 'org.knopflerfish.', 'org.LatencyUtils.',
    'org.locationtech.', 'org.mariadb.', 'org.mockito.', 'org.mortbay.',
    'org.msgpack.', 'org.mybatis.', 'org.neo4j.', 'org.noggit.', 'org.nutz.',
    'org.oasisopen.', 'org.objectweb.', 'org.objenesis.', 'org.omg.',
    'org.openjdk.', 'org.opentest4j.', 'org.ops4j.', 'org.osgi.', 'org.osoa.',
    'org.owasp.', 'org.pentaho.', 'org.picketbox.', 'org.postgresql.',
    'org.powermock.', 'org.python.', 'org.quartz.', 'org.reactivestreams.',
    'org.redisson.', 'org.relaxng.', 'org.rhq.', 'org.richfaces.',
    'org.roaringbitmap.', 'org.skyscreamer.', 'org.slf4j.', 'org.sonatype.',
    'org.springdoc.', 'org.springframework.', 'org.synchronoss.',
    'org.terracotta.', 'org.thymeleaf.', 'org.tukaani.', 'org.unbescape.',
    'org.w3c.', 'org.webjars.', 'org.wildfly.', 'org.xerial.', 'org.xml.',
    'org.xmlpull.', 'org.xmlunit.', 'org.xnio.', 'org.yaml.', 'org.znerd.',
    'oshi.', 'play.', 'reactor.', 'redis.', 'ru.yandex.', 'rx.', 'scala.',
    'serp.', 'sun.', 'weblogic.', 'workshop.', 'zipkin2.'
]
trie = marisa_trie.Trie(rules)
from typing import TypedDict, List


class CodeStack(TypedDict):
    stack: str
    code_belong: str


def stack_scan(stack: str,
               extend_black_list: list = [],
               extend_white_list: list = []) -> CodeStack:
    for rule in extend_white_list:
        stack.startswith(rule)
        return {"stack": stack, "code_belong": "user"}

    for rule in extend_black_list:
        stack.startswith(rule)
        return {"stack": stack, "code_belong": "system"}
    if stack in trie:
        return {"stack": stack, "code_belong": "system"}
    return {"stack": stack, "code_belong": "user"}


def stacks_convert(stacks: List[str],
                   extend_black_list=[],
                   extend_white_list=[]) -> List[CodeStack]:
    return list(
        map(lambda x: stack_scan(x, extend_black_list, extend_white_list),
            stacks))
